import csv
from datetime import datetime
class AirplaneData:
    def __init__(self, filepath):
        self.__AirplaneData = dict()
        self.airports = []
        with open(filepath, 'r') as airplaneFile:
            next(airplaneFile)
            airplaneFileReader = csv.reader(airplaneFile, delimiter=',')
            count = 0
            for row in airplaneFileReader:
                if (row[5][:2] == "EG"):
                    if (self.airports.count(row[5]) == 0):
                        self.airports.append(row[5])
                    date = datetime.utcfromtimestamp(int(row[2])).strftime("%Y-%m-%d")
                    key = (date, row[5])
                    print (count)
                    count += 1
                    if (list(self.__AirplaneData.keys()).count(key) == 1):
                        self.__AirplaneData[key] += 1
                    else:
                        self.__AirplaneData[key] = 1
    def getData(self, date, location):
        try:
            return self.__AirplaneData[(date, location)]
        except:
            return 0
    def getAirports(self):
        return self.airports

#TestCODE
a = AirplaneData("C:/Users/benji/Downloads/output.csv")
print(a.getAirports())
print(a.getData("2020-04-24", "KMDT")) #Accepts date in YEAR-MONTH-DAY and 