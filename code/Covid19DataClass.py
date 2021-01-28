import csv
class Covid19Data: #Class to load, store and retrieve covid 19 Data
    def __init__(self, filepath):
        self.__CovidData = dict() #Dictionary to store all covid data
        self.locations = [] #List to store all locations in
        with open(filepath, 'r') as covidFile:
            next(covidFile) #skipping the first line in the csv file
            covidFileReader = csv.reader(covidFile, delimiter=',') #splitting the csv file up by cells
            for row in covidFileReader: #reading each row
                if self.locations.count(row[3]) == 0: #Checking if the location has already been added to the unique location list
                    self.locations.append(row[3])
                key = (row[0], row[3]) #Creating a key to store the covid19 data in
                self.__CovidData[key] = row[4]
    def getData(self, date, location): #function to retrieve covid19 data for a specific date and location
        try:
            return self.__CovidData[(date, location)]
        except:
            return 0
    def getLocations(self): #Function to return the list of all of the locations of the 
        return self.locations

#TestCODE
a = Covid19Data("C:/Users/benji/Downloads/utla_2021-01-04.csv")
print(a.getLocations())
print(a.getData("12/01/2020", "Derry City and Strabane"))