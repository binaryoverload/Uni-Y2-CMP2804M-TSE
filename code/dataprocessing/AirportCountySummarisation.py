from datetime import datetime 
import os

import AirplaneDataClass as adc

airports, flightCount = adc.processData("../../data/flight-data-jan-dec.csv")
a = adc.AirplaneData(airports, flightCount)

airportCountyMapping = dict()

with open("../../data/airport-counties.csv", "r") as openFile:
    next(openFile)
    for row in openFile:
        rowData = row.split(",")
        airportCountyMapping[rowData[0].strip()] = rowData[1].strip()

countyData = dict()

invalidAirports = dict()

for key, count in a.getData().items():
    date, airport = key

    if not airport in airportCountyMapping:
        if not airport in invalidAirports:
            invalidAirports[airport] = 1
        else:
            invalidAirports[airport] += 1
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

for airport in invalidAirports:
    print(f"Could not find county for airport \"{airport}\" {invalidAirports[airport]} times")

if not os.path.exists("CountyAirport"):
    os.mkdir("CountyAirport")

with open("airport-county-flight-count.csv", "w") as airportCounts:
    airportCounts.write("date,county,count\n")
    for county in countyData:
        for date, count in sorted(countyData[county].items(), key=lambda item: item[0]):
            airportCounts.write(f"{date.strftime('%d/%m/%Y')},{county},{count}\n")
        