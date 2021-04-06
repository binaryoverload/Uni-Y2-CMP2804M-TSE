import csv
import json

fieldnames = (
    "date", "areaCode", "areaName", "numbOfCases", "numbOfNewCases"
)

with open('./covid-data-jan-dec.csv', 'r') as csvfile:
    with open('./covid-data-jan-dec.json', 'w') as jsonfile:
        # `next` will simply skip over the header row in the csvfile
        next(csvfile)

        reader = csv.DictReader(csvfile, fieldnames)

        final_data = {}

        for row in reader:

            final_data[row["date"]] = {
                "areaCode": row["areaCode"],
                "areaName": row["areaName"],
                "numbOfCases": row["numbOfCases"],
                "numbOfNewCases": row["numbOfNewCases"],
            }

        json.dump(final_data, jsonfile)

        jsonfile.write('\n')