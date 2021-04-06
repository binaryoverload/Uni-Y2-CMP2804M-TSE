import csv
import json

fieldnames = (
    "icao24", "firstSeen", "lastSeen", "callSign", "estDepartureAirport", "estArrivalAirport"
)

with open('./flight-data-jan-oct-international.csv', 'r') as csvfile:
    with open('./flight-data-international.json', 'w') as jsonfile:

        next(csvfile)

        reader = csv.DictReader(csvfile, fieldnames)

        final_data = {}

        for row in reader:

            final_data[row["icao24"]] = {
                "firstSeen": row["firstSeen"],
                "lastSeen": row["lastSeen"],
                "callSign": row["callSign"],
                "estDepartureAirport": row["estDepartureAirport"],
                "estArrivalAirport": row["estArrivalAirport"],
            }
        json.dump(final_data, jsonfile)

        jsonfile.write('\n')