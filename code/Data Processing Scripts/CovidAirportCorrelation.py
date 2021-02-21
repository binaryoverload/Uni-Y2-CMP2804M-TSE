import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time

dateFlightCount = dict()
covidCount = dict()

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

mergedData = []

fig, ax = plt.subplots()

for key in dateFlightCount.keys():
    #mergedData.append([dateFlightCount[key], covidCount[key]])
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

title = "Numbers of daily COVID-19 cases plotted against flights per day"

fig.canvas.set_window_title(title)

plt.title(title)
plt.show()