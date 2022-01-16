import datetime
from repositories.CarRepository import CarRepository
from repositories.OrderRepository import OrderRepository
class CarRentCheckServices():
    def __init__(self):
        self.__car_repo = CarRepository()
        self.__order_repo = OrderRepository()
        self.__cars = self.__car_repo.getCars()
        self.__orders = self.__order_repo.getOrders()

    def carReturnCheck(self):
        """
        Checks to see if the car is available when it shouldn't be
        and corrects it
        """
        now = datetime.datetime.now()
        for order in self.__orders:
            car = self.__cars[self.__orders[order].getCarPlate()]
            return_date = datetime.datetime.strptime(self.__orders[order].getReturnDate(), '%Y-%m-%d')
            if return_date < now and car.getStatus() != "Laus":
                updated_car = car
                updated_car.setStatus("Laus")
                self.__car_repo.deleteCar(car.getPlateNumber())
                self.__car_repo.addCar(updated_car)
        return None

    def carRentCheck(self):
        """
        Checks to see if the car isn't available when it should be
        and corrects it
        """
        now = datetime.datetime.now()
        for order in self.__orders:
            car = self.__cars[self.__orders[order].getCarPlate()]
            return_date = datetime.datetime.strptime(self.__orders[order].getReturnDate(), '%Y-%m-%d')
            rented_date = datetime.datetime.strptime(self.__orders[order].getRentedDate(), '%Y-%m-%d')
            if return_date > now and rented_date < now and car.getStatus() != "Útleigu":
                updated_car = car
                updated_car.setStatus("Útleigu")
                self.__car_repo.deleteCar(car.getPlateNumber())
                self.__car_repo.addCar(updated_car)
        return None