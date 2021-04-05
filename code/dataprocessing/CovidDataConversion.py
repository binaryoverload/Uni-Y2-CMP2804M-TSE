import csv
import json

output = []

fileName = "covid-data-jan-dec.old"

with open(f"../../data/{fileName}.csv", "r") as openFile:
    next(openFile) # Skip the header
    csvFileReader = csv.reader(openFile, delimiter=',')
    for data in csvFileReader:
        output.append([data[0],data[2],data[4],data[5]])

with open(f"../../data/{fileName}.converted.csv", "w") as writeFile:
    writeFile.write("date,areaCode,cumCasesBySpecimenDate,newCasesBySpecimenDate\n")
    for outputRow in output:
        writeFile.write(",".join(outputRow) + "\n")