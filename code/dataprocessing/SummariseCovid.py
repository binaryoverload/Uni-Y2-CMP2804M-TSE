import datetime 

covidDates = dict()

with open("../../data/covid-data-jan-dec.csv", "r") as openFile:
    next(openFile) # Skip the header
    for row in openFile:
        dateField = row.split(",")[0].split("/")
        date = datetime.date(int(dateField[2]), int(dateField[1]), int(dateField[0]))
        if date in covidDates:
            covidDates[date]["daily"] += int(row.split(",")[3])
            covidDates[date]["cumulative"] += int(row.split(",")[2])
        else:
            covidDates[date] = {
                "daily": int(row.split(",")[3]),
                "cumulative": int(row.split(",")[2])
            }

with open("covid-data-summarised.csv", "w") as airportCounts:
    airportCounts.write("date,daily,cumulative\n")
    for date, data in sorted(covidDates.items(), key=lambda item: item[0]):
        airportCounts.write(f"{date.strftime('%d/%m/%Y')},{data['cumulative']},{data['daily']}\n")