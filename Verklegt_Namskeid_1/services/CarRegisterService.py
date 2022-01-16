from models.Car import Car
from repositories.CarRepository import CarRepository
class CarRegisterService():
    """
    Class to register new vehicles and confirm that the written
    information about the new vehicle are correct (right format)
    """
    def __init__(self):
        self.__car_repository = CarRepository()
        self.__valid_car_type_choices = ["1","2","3","4"]
        self.__valid_fuel_type_choices = ["1","2","3"]

    def addCar(self, plate_number, status, car_type, seats, 
               fuel_type, model, price_range, manufacturer, 
               color):
        """
        Function to create a new vehicle to be kept in the database 'Cars.csv'
        """
        new_car = Car(plate_number, status, car_type, seats, 
                      fuel_type, model, price_range, manufacturer, 
                      color)
        self.__car_repository.addCar(new_car)
        return plate_number

    def isValidPlateNumber(self, plate_number):
        """
        A valid plate number uses this format CC CDD
        C = Character in the alphabet
        D = digit
        """
        if not len(plate_number) == 6:
            return False
        if not plate_number[2] == " ":
            return False
        if not plate_number[:2].isalpha() and plate_number[3].isalpha():
            return False
        if not plate_number[4:].isdigit():
            return False
        return True
        
    def isValidType(self, choice):
        """
        Checks if the car type is valid
        """
        return choice in self.__valid_car_type_choices

    def isValidFuel(self, choice):
        """
        Checks if the fuel type is valid
        """
        return choice in self.__valid_fuel_type_choices
    
    def isValidSeats(self, seats):
        """
        Checks if the number of seats is valid
        """
        return seats.isdigit()
    
    def isValidModel(self, model):
        """
        Checks if the model is valid
        """
        return model.isdigit()
    
    def isValidColor(self, color):
        """
        Checks if the color is valid
        """
        return color.isalpha()

    def isValidChange(self, choice):
        """
        Checks if the choice is valid
        """
        return choice == "j" or choice == "n"
    