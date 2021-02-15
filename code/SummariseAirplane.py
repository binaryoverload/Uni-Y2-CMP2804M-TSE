import csv
from datetime import datetime
import AirplaneDataClass as adc

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

airports, flightCount = adc.processData("FilteredFile.csv")
a = adc.AirplaneData(airports, flightCount)

airportFlightCount = dict()
dateFlightCount = dict()

for key, count in a.getData().items():
    date, airport = key

    if airport in airportFlightCount:
        airportFlightCount[airport] += count
    else:
        airportFlightCount[airport] = count

    year, month, day = date
    numpy_date = np.datetime64(f'{year}-{month:02d}-{day:02d}')
    dt = datetime.fromisoformat(f'{year}-{month:02d}-{day:02d}')

    if dt in dateFlightCount:
        dateFlightCount[dt] += count
    else:
        dateFlightCount[dt] = count

for airport, count in sorted(airportFlightCount.items(), key=lambda item: item[0]):
    print(airport+":", count)

for date, count in sorted(dateFlightCount.items(), key=lambda item: item[0]):
    print(date.strftime("%Y-%m-%d")+":", count)

data = np.array(list(dateFlightCount.items()))


fig, ax = plt.subplots()
plt.plot_date(dateFlightCount.keys(), dateFlightCount.values(), 'rx')

locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

# # round to nearest years.
datemin = np.datetime64(data[0][0], 'Y')
datemax = np.datetime64(data[-1][0], 'Y') + np.timedelta64(1, 'Y')

ax.set_xlim(datemin, datemax)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = lambda y: int(y)  # format the price.
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()
fig.canvas.set_window_title('UK Destination Flight Count March - Oct 2020')

plt.show()