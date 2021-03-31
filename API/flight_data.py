import csv
import json

# Define the header names so we can specify them when reading the CSV
fieldnames = (
    "icao24", "firstSeen", "lastSeen", "callSign", "estDepartureAirport", "estArrivalAirport"
)

# Open both files so we can interact with them
# Using the `with` keyword lets us close the files automatically after these
# with blocks end and we're done writing and reading the files
with open('./flight-data-jan-dec.csv', 'r') as csvfile:
    with open('./flight-data-jan-dec.json', 'w') as jsonfile:
        # `next` will simply skip over the header row in the csvfile
        next(csvfile)
        # We use the csv library to create a 'reader' of the file
        # This reader passes through the csvfile and the headers
        # and allow us to interact with it as a Python object
        reader = csv.DictReader(csvfile, fieldnames)
        # This creates an empty dictionary to hold the final set of
        # data that gets dumped into the JSON file
        final_data = {}
        # use the reader to iterate over all the rows of the CSV
        # (except for the header) and then keep the values we want
        for row in reader:
            # restructure the data so that it exists as
            # a set of date keys with the value as a dictionary of
            # different data elements from the CSV.
            final_data[row["icao24"]] = {
                "firstSeen": row["firstSeen"],
                "lastSeen": row["lastSeen"],
                "callSign": row["callSign"],
                "estDepartureAirport": row["estDepartureAirport"],
                "estArrivalAirport": row["estArrivalAirport"],
            }
        # Finally, we use the json library to output the final_data
        # dictionary to the jsonfile we opened earlier
        json.dump(final_data, jsonfile)

        jsonfile.write('\n')