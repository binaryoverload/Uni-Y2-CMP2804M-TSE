import csv
class AirportCounties:
    def __init__(self, fileLocation):
        self.airportCounties = dict()
        with open(fileLocation, 'r') as file:
            next(file) #skipping the column names
            AirportCountiesReader = csv.reader(file, delimiter=',')
            for row in AirportCountiesReader:
                if row[1] in self.airportCounties:
                    self.airportCounties[row[1]].append(row[0])
                else:
                    self.airportCounties[row[1]] = [row[0]]
    def getAirportsInCounty(self, CountyCode):
        return self.airportCounties[CountyCode]
#Example init code    
#a = AirportCounties("AirportCounties.csv")