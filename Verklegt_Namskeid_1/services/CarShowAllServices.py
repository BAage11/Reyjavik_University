from repositories.CarRepository import CarRepository
class CarShowAllServices():
    def __init__(self):
        self.__car_repository = CarRepository()
        self.__cars = self.__car_repository.getCars()
        self.__valid_choices = ["0"]

    def getCars(self):
        """
        Returns all cars
        """
        return self.__cars

    def createValidChoices(self):
        """
        Creates all valid choices
        """
        for customer_ssn in self.__cars:
            self.__valid_choices.append(customer_ssn)
        return None
    
    def isValidChoice(self, choice):
        """
        Checks if the users choice is valid
        """
        return choice in self.__valid_choices
    
    