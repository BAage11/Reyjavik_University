import os
from services.CarRemoveServices import CarRemoveServices
class CarRemoveUi():
    def __init__(self):
        self.__remove_car_services = CarRemoveServices()
    
    def carRemoveMenu(self):
        """
        The user selects a car to remove
        """
        os.system('cls')
        print("------- Fjarlægja bíl -------")
        plate = self.getPlate()
        self.__remove_car_services.removeCar(plate)
        print("Bíll hefur verið fjarlægður")
    
    def getPlate(self):
        """
        The user inputs a plate number
        """
        plate = input("{}".format("Númeraplata bíls: "))
        while self.__remove_car_services.isValidPlate(plate) == False:
            print("Enginn bíll er með þessa númeraplötu")
            plate = input("{}".format("Númeraplata bíls: "))
        return plate