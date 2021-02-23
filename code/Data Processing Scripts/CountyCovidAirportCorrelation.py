import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time
import os
from textwrap import wrap



def removeFileExt(fileName):
    return fileName[0:(fileName.rfind("."))].strip()

counties = list(map(removeFileExt, os.listdir("CountyAirport/")))

if not os.path.exists("CountyPlots"):
    os.mkdir("CountyPlots")

for county in counties:

    dateFlightCount = dict()
    covidCount = dict()

    with open(f"CountyAirport/{county}.csv", "r") as openFile:
        next(openFile) # Skip the header
        for row in openFile:
            dt = datetime.fromisoformat(row.split(",")[0])
            count = int(row.split(",")[1])
            if dt in dateFlightCount:
                dateFlightCount[dt] += count
            else:
                dateFlightCount[dt] = count
                
    if not os.path.exists(f"CountyCovid/{county}.csv"):
        print(f"Covid data for county {county} doesn't exist!")
        continue
    with open(f"CountyCovid/{county}.csv", "r") as openFile:
        next(openFile) # Skip the header
        for row in openFile:
            dt = datetime.fromisoformat(row.split(",")[0])
            count = int(row.split(",")[1])
            if dt in covidCount:
                covidCount[dt] += count
            else:
                covidCount[dt] = count

    mergedData = []

    fig, ax = plt.subplots()

    for key in dateFlightCount.keys():
        #mergedData.append([dateFlightCount[key], covidCount[key]])
        if key in covidCount:
            plt.plot(covidCount[key], dateFlightCount[key], "bx")

    #plt.plot(mergedData)

    # format the coords message box
    ax.format_xdata = lambda x: int(x)
    ax.format_ydata = lambda y: int(y)  # format the price.
    ax.grid(True)

    ax.set_ylabel('COVID-19 Cases')
    ax.set_xlabel('Flights')

    # rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them
    fig.autofmt_xdate()

    title = "Numbers of daily COVID-19 cases plotted against flights per day in the county " + county

    title = "\n".join(wrap(title, 60))

    fig.canvas.set_window_title(title)

    plt.title(title)
    plt.savefig(f"CountyPlots/{county}.png")
    plt.close()