import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

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

fig, ax = plt.subplots()
plt.plot_date(dateFlightCount.keys(), dateFlightCount.values(), 'rx')

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = lambda y: int(y)  # format the price.
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()
fig.canvas.set_window_title('Incoming UK Flight Count March - Oct 2020')

plt.title('Incoming UK Flight Count March - Oct 2020')
plt.show()