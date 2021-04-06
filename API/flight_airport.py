import csv
import json

fieldnames = (
    "icao24", "callSign", "estArrivalAirport"
)

with open('./flight-data-jan-dec.csv', 'r') as csvfile:
    with open('./flight-data-aiports.json', 'w') as jsonfile:

        next(csvfile)

        reader = csv.DictReader(csvfile, fieldnames)

        final_data = {}

        for row in reader:

            final_data[row["icao24"]] = {
                "callSign": row["callSign"],
                "estArrivalAirport": row["estArrivalAirport"],
            }
        json.dump(final_data, jsonfile)

        jsonfile.write('\n')