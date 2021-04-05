import csv
from datetime import datetime
import AirplaneDataClass as adc

airports, flightCount = adc.processData("../../data/flight-data-jan-dec.csv")
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
    dt = datetime.fromisoformat(f'{year}-{month:02d}-{day:02d}')

    if dt in dateFlightCount:
        dateFlightCount[dt] += count
    else:
        dateFlightCount[dt] = count

with open("airport-flight-count.csv", "w") as airportCounts:
    airportCounts.write("airport,count\n")
    for airport, count in sorted(airportFlightCount.items(), key=lambda item: item[1]):
        airportCounts.write(f"{airport},{count}\n")    

with open("date-flight-count.csv", "w") as airportCounts:
    airportCounts.write("date,count\n")
    for date, count in sorted(dateFlightCount.items(), key=lambda item: item[0]):
        airportCounts.write(f"{date.strftime('%d/%m/%Y')},{count}\n")