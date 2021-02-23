import datetime 
import os

countyData = dict()

with open("../../data/covid-data.csv", "r") as openFile:
    next(openFile) # Skip the header
    for row in openFile:
        dateField = row.split(",")[0].split("/")
        date = datetime.date(int(dateField[2]), int(dateField[1]), int(dateField[0]))
        county = row.split(",")[2]
        if county in countyData:
            countyDict = countyData[county]
            if date in countyDict:
                countyDict[date] += int(row.split(",")[5])
            else:
                countyDict[date] = int(row.split(",")[5])
        else:
            countyDict = dict()
            countyDict[date] = int(row.split(",")[5])
            countyData[county] = countyDict


if not os.path.exists("CountyCovid"):
    os.mkdir("CountyCovid")

for county in countyData:
    with open("CountyCovid/" + county + ".csv", "w") as covidCounts:
        covidCounts.write("date,count\n")
        for date, count in sorted(countyData[county].items(), key=lambda item: item[0]):
            covidCounts.write(f"{date.strftime('%Y-%m-%d')},{count}\n")