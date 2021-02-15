import datetime 

covidDates = dict()

with open("../data/covid-data.csv", "r") as openFile:
    next(openFile) # Skip the header
    for row in openFile:
        dateField = row.split(",")[0].split("/")
        date = datetime.date(int(dateField[2]), int(dateField[1]), int(dateField[0]))
        if date in covidDates:
            covidDates[date] += int(row.split(",")[5])
        else:
            covidDates[date] = int(row.split(",")[5])

with open("covid-data-summarised.csv", "w") as airportCounts:
    airportCounts.write("date,count\n")
    for date, count in sorted(covidDates.items(), key=lambda item: item[0]):
        airportCounts.write(f"{date.strftime('%Y-%m-%d')},{count}\n")