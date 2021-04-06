import csv
import json

fieldnames = (
    "date", "areaCode", "areaName", "numbOfCases"
)

with open('./covid-data-jan-dec.csv', 'r') as csvfile:
    with open('./covid-data-county.json', 'w') as jsonfile:

        next(csvfile)

        reader = csv.DictReader(csvfile, fieldnames)

        final_data = {}

        for row in reader:

            final_data[row["areaCode"]] = {
                "date": row["date"],
                "areaName": row["areaName"],
                "numbOfCases": row["numbOfCases"],
            }

        json.dump(final_data, jsonfile)

        jsonfile.write('\n')