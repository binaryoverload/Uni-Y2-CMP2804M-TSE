import csv
from datetime import datetime

def processData(filepath):
    airports = []
    flightCount = dict()
    with open(filepath, 'r') as airplaneFile:
            next(airplaneFile)
            airplaneFileReader = csv.reader(airplaneFile, delimiter=',')
            validCount = 0
            rowCount = 0
            for row in airplaneFileReader:
                rowCount += 1
                if row[5][:2] == "EG": # Check that the destination is in the UK
                    if not row[5] in airports:
                        airports.append(row[5])
                    
                    date = datetime.utcfromtimestamp(int(row[2]))
                    key = ((date.year, date.month, date.day), row[5])
                    
                    if validCount % 1000 == 0:
                        print("Accepted data:", validCount, "|", "Row count:", rowCount)

                    validCount += 1

                    if key in flightCount:
                        flightCount[key] += 1
                    else:
                        flightCount[key] = 1
            print("Accepted data:", validCount, "|", "Row count:", rowCount)
    return (airports, flightCount)


class AirplaneData:
    def __init__(self, airports, flightCount):
        self.flightCount = flightCount
        self.airports = airports
                    
    def getFlightCount(self, year, month, day, location):
        try:
            return self.flightCount[((year, month, day), location)]
        except:
            return 0

    def getData(self):
        return self.flightCount
    
    def getAirports(self):
        return self.airports