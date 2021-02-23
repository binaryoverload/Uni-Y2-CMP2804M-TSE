from datetime import datetime 
import os

import AirplaneDataClass as adc

airports, flightCount = adc.processData("../../data/flight-data-filtered.csv")
a = adc.AirplaneData(airports, flightCount)

airportCountyMapping = dict()

with open("../../data/airport-counties.csv", "r") as openFile:
    next(openFile)
    for row in openFile:
        rowData = row.split(",")
        airportCountyMapping[rowData[0].strip()] = rowData[1].strip()

countyData = dict()

for key, count in a.getData().items():
    date, airport = key

    if not airport in airportCountyMapping:
        print("Could not find county for airport: " + airport)
        continue

    county = airportCountyMapping[airport]

    year, month, day = date
    dt = datetime.fromisoformat(f'{year}-{month:02d}-{day:02d}')

    if county in countyData:
        countyDict = countyData[county]
        if date in countyDict:
            countyDict[dt] += count
        else:
            countyDict[dt] = count
    else:
        countyDict = dict()
        countyDict[dt] = count
        countyData[county] = countyDict

if not os.path.exists("CountyAirport"):
    os.mkdir("CountyAirport")

for county in countyData:
    with open("CountyAirport/" + county + ".csv", "w") as airportCounts:
        airportCounts.write("date,count\n")
        for date, count in sorted(countyData[county].items(), key=lambda item: item[0]):
            airportCounts.write(f"{date.strftime('%Y-%m-%d')},{count}\n")