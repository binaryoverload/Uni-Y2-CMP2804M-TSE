import csv

with open('flight-data.csv') as csv_file:

    myFile = csv.reader(csv_file)
    
    recordCount = 0

    headerRow = next(myFile)

    with open('../data/flight-data-filtered.csv', mode='w', newline='') as FilteredFile:
        record_writer = csv.writer(FilteredFile)
        record_writer.writerow(headerRow)
        for row in myFile:
            if row[5][:2] == "EG":
                recordCount += 1
                if recordCount % 500 == 0:
                    print("Processed", recordCount, "rows")
                appendRecord = row

                record_writer.writerow(appendRecord)
