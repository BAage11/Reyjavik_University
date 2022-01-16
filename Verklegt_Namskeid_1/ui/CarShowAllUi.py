import os
from services.CarShowAllServices import CarShowAllServices
from ui.CarSpecificUi import CarSpecificUi
class CarShowAllUi():
    def __init__(self):
        self.__all_car_services = CarShowAllServices()
        self.__cars_dict = self.__all_car_services.getCars()
        self.__cars_list = [car for car in self.__cars_dict.values() if(car.getStatus() == "Laus")]

    def printInformation(self):
        """
        Prints out the number plate for each car and the type of the car
        """
        self.__cars_list = [car for car in self.__cars_dict.values() if(car.getStatus() == "Laus")]
        os.system('cls')
        print("------ Lausir Bílar -----")
        for car in self.__cars_list:
            print("{} {}".format((car.getPlateNumber() + ":"),
                                 car.getCarType()))
        print("-------------------------")
        self.selectSpecificCar()
        return None

    def selectSpecificCar(self):
        """
        The user inputs a car plate and chooses a car
        """
        print("Veldu bíl til að fá nánari upplýsingar um")
        print("stimplaðu inn númeraplötu til að velja bíl")
        print("0. Til að hætta")
        choice = input("> ")
        self.__all_car_services.createValidChoices()
        while self.__all_car_services.isValidChoice(choice) == False:
            print(choice,"Er ekki lögleg aðgerð, reyndu aftur")
            choice = input("> ")
        if choice == "0":
            return None 
        specific_car_ui = CarSpecificUi(choice) 
        specific_car_ui.printInformation()