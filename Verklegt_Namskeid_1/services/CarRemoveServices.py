from repositories.CarRepository import CarRepository
class CarRemoveServices():
    def __init__(self):
        self.__car_repo = CarRepository()
        self.__cars = self.__car_repo.getCars()

    def isValidPlate(self, plate):
        """
        Checks if the plate is valid
        """
        return plate in self.__cars

    def removeCar(self, plate_number):
        """
        Removes a car
        """
        self.__car_repo.deleteCar(plate_number)