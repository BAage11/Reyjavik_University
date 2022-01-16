from repositories.OrderRepository import OrderRepository
from repositories.CarRepository import CarRepository
class CarSpecificServices():
    def __init__(self):
        self.__car_repository = CarRepository()
        self.__order_repository = OrderRepository()
        self.__cars = self.__car_repository.getCars()
        self.__orders = self.__order_repository.getOrders()

    def getCar(self, plate_number):
        """
        Returns specific car
        """
        self.__cars = self.__car_repository.getCars()
        return self.__cars[plate_number]

    def findOrders(self, plate_number):
        """
        Returns all orders for a specific car
        """
        car_orders = []
        for order in self.__orders:
            if self.__orders[order].getCarPlate() == plate_number:
                car_orders.append(self.__orders[order])
        return car_orders