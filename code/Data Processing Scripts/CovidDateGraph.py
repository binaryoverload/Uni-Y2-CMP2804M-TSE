import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time

covidCount = dict()
dateFlightCount = dict()

with open("date-flight-count.csv", "r") as openFile:
    next(openFile) # Skip the header
    for row in openFile:
        dt = datetime.fromisoformat(row.split(",")[0])
        count = int(row.split(",")[1])
        if dt in dateFlightCount:
            dateFlightCount[dt] += count
        else:
            dateFlightCount[dt] = count

with open("covid-data-summarised.csv", "r") as openFile:
    next(openFile) # Skip the header
    for row in openFile:
        dt = datetime.fromisoformat(row.split(",")[0])
        count = int(row.split(",")[1])
        if dt in covidCount:
            covidCount[dt] += count
        else:
            covidCount[dt] = count

fig, covidAx = plt.subplots()

flightAx = covidAx.twinx()

for key in covidCount.keys():
    #mergedData.append([dateFlightCount[key], covidCount[key]])
    covidAx.plot(key, covidCount[key], "bx")
    if key in dateFlightCount:
        flightAx.plot(key, dateFlightCount[key], "rx")

covidAx.format_xdata = lambda x: x
covidAx.grid(True)

covidAx.set_xlabel('Dates')
covidAx.set_ylabel('COVID-19 Cases', color='tab:blue')
covidAx.tick_params(axis='y', labelcolor='tab:blue')


flightAx.set_ylabel('Flights', color='tab:red')
flightAx.tick_params(axis='y', labelcolor='tab:red')


# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

title = "Number of COVID-19 cases compared against Flights"

fig.canvas.set_window_title(title)

plt.title(title)
plt.show()