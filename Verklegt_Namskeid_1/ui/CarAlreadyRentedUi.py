from services.CarAlreadyRentedServices import CarAlreadyRentedServices
from ui.CarSpecificUi import CarSpecificUi
import os
class CarAlreadyRentedUi():
    def __init__(self):
        self.__car_already_rented_services = CarAlreadyRentedServices()
        #self.__cars = self.__car_already_rented_services.getCarsNotAvailabe()
        self.__cars_dict = self.__car_already_rented_services.getCars()
        self.__cars_list = [car for car in self.__cars_dict.values() if(car.getStatus() == "Útleigu")]


    def printInformation(self):
        """
        Prints out the number plate for each car and the type of the car
        """
        self.__cars_list = [car for car in self.__cars_dict.values() if(car.getStatus() == "Útleigu")]
        os.system('cls')
        print("---- Bílar Í Útleigu ----")
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
        self.__car_already_rented_services.createValidChoices()
        while self.__car_already_rented_services.isValidChoice(choice) == False:
            print(choice, "Er ekki lögleg aðgerð, reyndu aftur")
            choice = input("> ")
        if choice == "0":
            return None
        specific_car_ui = CarSpecificUi(choice)
        specific_car_ui.printInformation()
