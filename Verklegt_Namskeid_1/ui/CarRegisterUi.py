import os
from services.CarRegisterService import CarRegisterService
from ui.CarRegisterChangeUi import CarRegisterChangeUi
class CarRegisterUi():
    def __init__(self):
        self.__car_service = CarRegisterService()
        self.__car_change = CarRegisterChangeUi()
        self.__plate_number = "" 
        self.__status = "Laus"
        self.__car_type = ""
        self.__seats = ""
        self.__fuel_type = ""
        self.__model = ""
        self.__price_range = "" 
        self.__manufacturer = ""
        self.__color = ""
        self.__car_types = {"1":"Jeppi", "2":"Jepplingur", "3":"Fólksbíll", "4":"Smábíll"}
        self.__car_fuels = {"1":"Rafmagn", "2":"Okt-95", "3":"Dísel"}
        self.__car_prices = {"Jeppi":"20.000", "Jepplingur":"15.000", "Fólksbíll":"12.000", "Smábíll":"10.000"}

    def addCarMenu(self):
        """
        The user registers a car by inputting the neccesary information
        """
        os.system('cls')
        print("--------- Nýskrá Bíl ----------")
        self.__plate_number = self.getPlateNumber()
        self.__car_type = self.getCarType()
        self.__seats = self.getSeats()
        self.__fuel_type = self.getFuelType()
        self.__model = self.getModel()
        self.__manufacturer = self.getManufacturer()
        self.__color = self.getColor()
        print("-------------------------------")
        self.__price_range = self.getPriceRange(self.__car_type)
        self.__car_service.addCar(self.__plate_number, self.__status, self.__car_type, self.__seats, 
                                  self.__fuel_type, self.__model, self.__price_range, self.__manufacturer, 
                                  self.__color)
        print("BÍLL HEFUR VERIÐ SKRÁÐUR!")
        self.changeCar(self.__plate_number)
        return None

    def getPlateNumber(self):
        """
        The user inputs a plate number
        """
        plate_number = input("{:<15}".format("Númeraplata:"))
        while self.__car_service.isValidPlateNumber(plate_number) == False:
            print("Þetta er ekki lögleg númeraplata!")
            plate_number = input("{:<15}".format("Númeraplata:"))
        return plate_number
    
    def getSeats(self):
        """
        The user inputs the number of seats
        """
        seats = input("{:<15}".format("Fjöldi Sæta:"))
        while self.__car_service.isValidSeats(seats) == False:
            print("Þetta er ekki löglegt númer sæta!")
            seats = input("{:<15}".format("Fjöldi sæta:"))
        return seats
    
    def getModel(self):
        """
        The user inputs the car model
        """
        model = input("{:<15}".format("Árgerð:"))
        while self.__car_service.isValidModel(model) == False:
            print("Þetta er ekki lögleg árgerð!")
            model = input("{:<15}".format("Fjöldi sæta:"))
        return model
    
    def getPriceRange(self, car_type):
        """
        Returns the price range of the car
        """
        return self.__car_prices[car_type]
    
    def getManufacturer(self):
        """
        Returns the manufacturer of the car
        """
        return input("{:<15}".format("Tegund bíls:"))
    
    def getColor(self):
        """
        The user inputs a color
        """
        color = input("{:<15}".format("Litur:"))
        while self.__car_service.isValidColor(color) == False:
            print("Þetta er ekki löglegur litur!")
            color = input("{:<15}".format("Litur:"))
        return color

    def getCarType(self):
        """
        The user inputs what cartype the car is
        """
        print("Hvaða týpa er þessi bíll?")
        print("\t1. Jeppi")
        print("\t2. Jepplingur")
        print("\t3. Fólksbíll")
        print("\t4. Smábíll")
        choice = input("\t> ")
        while self.__car_service.isValidType(choice) == False:
            print("Þetta er ekki lögleg aðgerð!")
            choice = input("\t> ")
        return self.__car_types[choice]

    def getFuelType(self):
        """
        The user inputs what fuel the car uses
        """
        print("Hvaða orkugjafa hefur bíllinn?")
        print("\t1. Rafmagn")
        print("\t2. Okt-95")
        print("\t3. Dísel")
        choice = input("\t> ")
        while self.__car_service.isValidFuel(choice) == False:
            print("Þetta er ekki lögleg aðgerð!")
            choice = input("\t> ")
        return self.__car_fuels[choice]

    def changeCar(self, plate):
        choice = input("Viltu breyta einhverju?(j/n)").lower()
        while self.__car_service.isValidChange(choice) == False:
            print(choice, "Er hvorki j eða n")
            choice = input("Villtu breyta eitthverju?(j/n)").lower().strip()
        if choice == "j":
            self.__car_change.carRegisterChangeMainUi(self.__plate_number)
        return None
        