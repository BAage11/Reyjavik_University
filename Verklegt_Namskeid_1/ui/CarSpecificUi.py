import os
from services.CarSpecificServices import CarSpecificServices
class CarSpecificUi():
    def __init__(self, plate_number):
        self.__specific_car_services = CarSpecificServices()
        self.__car = self.__specific_car_services.getCar(plate_number)

    def printInformation(self):
        """
        Prints out the information about a specific car
        """
        os.system('cls')
        print("------------- {} -------------".format(self.__car.getPlateNumber()))
        print(self.__car)
        orders = self.__specific_car_services.findOrders(self.__car.getPlateNumber())
        for i in range(len(orders)):
            print("---------- Pöntun {} ----------".format(i+1))
            print(str(orders[i]))
            print("------------------------------")
        print("Ýttu á enter til að halda áfram")
        input("")
        return None
