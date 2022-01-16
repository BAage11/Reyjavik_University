from repositories.OrderRepository import OrderRepository
from repositories.CarRepository import CarRepository
import datetime


class CarAlreadyRentedServices():
    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__car_repo = CarRepository()
        self.__orders = self.__order_repo.getOrders()
        self.__cars = self.__car_repo.getCars()
        self.__valid_choices = ["0"]

    def getCarsNotAvailabe(self):
        """
        Gets all the cars that aren't available
        """
        cars = {}
        for order in self.__orders:
            if datetime.datetime.strptime(self.__orders[order].getRentedDate(), "%Y-%m-%d")\
                    < datetime.datetime.today() <\
                    datetime.datetime.strptime(self.__orders[order].getReturnDate(), "%Y-%m-%d"):
                number_plate = self.__orders[order].getCarPlate()
                cars[number_plate] = self.__cars[number_plate]
        return cars

    def getCars(self):
        return self.__car_repo.getCars()

    def createValidChoices(self):
        """
        Creates all the valid choices
        """
        for customer_ssn in self.__cars:
            self.__valid_choices.append(customer_ssn)
        return None

    def isValidChoice(self, choice):
        """
        Checks if the users choice is valid
        """
        return choice in self.__valid_choices