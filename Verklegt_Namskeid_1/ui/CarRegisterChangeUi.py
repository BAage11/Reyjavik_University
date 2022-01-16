import os
from models.Car import Car
from services.CarChangeServices import CarChangeServices
from services.CarRegisterService import CarRegisterService
class CarRegisterChangeUi():
    def __init__(self):
        self.__car_services = CarChangeServices()
        self.__register_services = CarRegisterService()
        self.__save = True
        self.__car_types = {"1":"Jeppi", "2":"Jepplingur", "3":"Fólksbíll", "4":"Smábíll"}
        self.__car_fuels = {"1":"Rafmagn", "2":"Okt-95", "3":"Dísel"}
        self.__car_prices = {"Jeppi":"20.000", "Jepplingur":"15.000", "Fólksbíll":"12.000", "Smábíll":"10.000"}
   
    def carRegisterChangeMainUi(self, plate):
        self.__car = self.__car_services.getCar(plate)
        os.system('cls')
        while self.__save:
            print("---------- Breyta Bíl ---------")
            print("1. " + self.__car.getPlateNumber())
            print("2. " + self.__car.getCarType())
            print("3. " + self.__car.getSeats())
            print("4. " + self.__car.getFuelType())
            print("5. " + self.__car.getModel())
            print("6. " + self.__car.getManufacturer())
            print("7. " + self.__car.getColor())
            print("8. Vista")
            print("-------------------------------")
            print("Hvað villtu breyta?")
            self.executeChoice(self.getChoice())
    
    def getChoice(self):
        """
        Gets what the user inputs as his choice
        """
        choice = input("> ")
        while not self.__car_services.isValidChoice(choice):
            print(choice,"Er ekki lögleg aðgerð")
            choice = input("> ")
        return choice
    
    def executeChoice(self, choice):
        """
        Executes the users choice
        """
        if choice == "1":
            new_value = self.getPlateNumber()
            self.__car_services.changePlate(new_value)
        elif choice == "2":
            new_value = self.getCarType()
            self.__car_services.changeCarType(new_value)
        elif choice == "3":
            new_value = self.getSeats()
            self.__car_services.changeSeats(new_value)
        elif choice == "4":
            new_value = self.getFuelType()
            self.__car_services.changeFuelType(new_value)
        elif choice == "5":
            new_value = self.getModel()
            self.__car_services.changeModel(new_value)
        elif choice == "6":
            new_value = self.getManufacturer()
            self.__car_services.changeManufacturer(new_value)
        elif choice == "7":
            new_value = self.getColor()
            self.__car_services.changeColor(new_value)
        elif choice == "8":
            self.__save = False
            return None

    def getPlateNumber(self):
        """
        The user inputs a plate number
        """
        plate_number = input("{:<15}".format("Númeraplata:"))
        while self.__register_services.isValidPlateNumber(plate_number) == False:
            print("Þetta er ekki lögleg númeraplata!")
            plate_number = input("{:<15}".format("Númeraplata:"))
        return plate_number
    
    def getSeats(self):
        """
        The user inputs the number of seats
        """
        seats = input("{:<15}".format("Fjöldi Sæta:"))
        while self.__register_services.isValidSeats(seats) == False:
            print("Þetta er ekki löglegt númer sæta!")
            seats = input("{:<15}".format("Fjöldi sæta:"))
        return seats
    
    def getModel(self):
        """
        The user inputs the car model
        """
        model = input("{:<15}".format("Árgerð:"))
        while self.__register_services.isValidModel(model) == False:
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
        while self.__register_services.isValidColor(color) == False:
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
        choice = input("\t>")
        while self.__register_services.isValidType(choice) == False:
            print("Þetta er ekki lögleg aðgerð!")
            choice = input("\t>")
        return self.__car_types[choice]

    def getFuelType(self):
        """
        The user inputs what fuel the car uses
        """
        print("Hvaða orkugjafa hefur bíllinn?")
        print("\t1. Rafmagn")
        print("\t2. Okt-95")
        print("\t3. Dísel")
        choice = input("\t>")
        while self.__register_services.isValidFuel(choice) == False:
            print("Þetta er ekki lögleg aðgerð!")
            choice = input("\t>")
        return self.__car_fuels[choice]
        