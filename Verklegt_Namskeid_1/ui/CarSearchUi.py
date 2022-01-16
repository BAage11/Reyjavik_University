import os
from services.CarSearchServices import CarSearchServices
class CarSearchUi():
    def __init__(self):
        self.__search_services = CarSearchServices()
        self.__choices = {"1":"Jeppi", "2":"Jepplingur", "3":"Fólksbíll", "4":"Smábíll"}

    def searchCarMenu(self):
        """
        Prints out the menu and gets all the data to search for a car
        """
        os.system('cls')
        print("-------- Leita að bíl --------")
        print("{:>15}".format("Dagsetning frá: "))
        from_date = self.getDate()
        print("{:>15}".format("Dagsetning til: "))
        return_date = self.getDate(from_date)
        print("------------------------------")
        car_type = self.getCarType()
        car = self.getAvailableCars(from_date, return_date, car_type)
        return from_date, return_date, car
    
    def getDate(self, from_date = 0):
        """
        Gets the date from the user
        """
        if from_date == 0:
            year = self.getYear()
            month = self.getMonth(year)
            day = self.getDay(month, year)
        else:
            year = self.getYear(from_date)
            month = self.getMonth(year, from_date)
            day = self.getDay(month, year, from_date)
        return "{}-{}-{}".format(year, month, day)

    def getYear(self, from_date = 0):
        """
        Gets the year from the user
        """
        year = input("\t{:>5}".format("Ár: "))
        while self.__search_services.isValidYear(year, from_date) == False:
            print(year, "Er ekki löglegt ár")
            year = input("\t{:>5}".format("Ár: "))
        return year
    
    def getMonth(self, year, from_date = 0):
        """
        Gets the month from the user
        """
        month = input("\t{:>5}".format("Mán: "))
        while self.__search_services.isValidMonth(month, year, from_date) == False:
            print(month, "Er ekki löglegur mánuður")
            month = input("\t{:>5}".format("Mán: "))
        return month
    
    def getDay(self, month, year, from_date = 0):
        """
        Gets the day from the user
        """
        day =  input("\t{:>5}".format("Dag: "))
        while self.__search_services.isValidDay(day, month, year, from_date) == False:
            print(day, "Er ekki löglegur dagur")
            day =  input("\t{:>5}".format("Dag: "))
        return day

    def getCarType(self):
        """
        Gets the user to select what car type he is looking for
        """
        print("Hvernig týpu er verið að leita að?")
        print("1. Jeppi, 20.000kr")
        print("2. Jepplingur, 15.000kr")
        print("3. Fólksbíll, 12.000kr")
        print("4. Smábíll, 10.000kr")
        choice = input(">")
        while self.__search_services.isValidChoice(choice) == False:
            print("Þetta er ekki lögleg aðgerð!")
            choice = input("> ")
        return self.__choices[choice]
    
    def selectCar(self, cars):
        """
        Gets the user to select a car
        """
        print("Veldu bíl")
        choice = input("> ")
        while self.__search_services.isValidCar(choice, len(cars)) == False:
            print("Þetta er ekki lögleg aðgerð!")
            choice = input("> ")
        return cars[int(choice) - 1]

    def getAvailableCars(self, from_date, return_date, car_type):
        """
        Gets all available cars and prints them out
        """
        cars = self.__search_services.getValidCars(from_date, return_date, car_type)
        for i in range(len(cars)):
            print("------------ Bíll {} ------------".format(i+1))
            print(cars[i])
            print("--------------------------------")
        car = self.selectCar(cars)
        return car
