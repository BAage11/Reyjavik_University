from repositories.CarRepository import CarRepository
class CarChangeServices():
    """
    Class to change the information written in the database 'Cars.csv'
    Information retreived about the car being changed with the plate number
    """
    def __init__(self):
        self.__car_repository = CarRepository()
        self.__valid_choices = ["1", "2", "3", "4",
                                "5", "6", "7", "8"]
        self.__car = ""

    def getCar(self, plate):
        """
        Gets the car information based on the given license plate of the vehicle
        """
        cars = self.__car_repository.getCars()
        self.__car = cars[plate]
        return cars[plate]

    def isValidChoice(self, choice):
        """
        Checks to see if the choice of the user is a valid choice,
        based on the given choices available for this menu
        """
        return choice in self.__valid_choices
    
    def changePlate(self, new_plates):
        """
        Changes the plate number of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setPlateNumber(new_plates)
        self.__car_repository.addCar(self.__car)

    def changeCarType(self, new_car_type):
        """
        Changes the car type of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setCarType(new_car_type)
        self.__car_repository.addCar(self.__car)

    def changeSeats(self, new_seats):
        """
        Changes the number of seats of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setSeats(new_seats)
        self.__car_repository.addCar(self.__car)

    def changeFuelType(self, new_fuel_type):
        """
        Changes the fuel type of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setFuelType(new_fuel_type)
        self.__car_repository.addCar(self.__car)
    
    def changeModel(self, new_model):
        """
        Changes the model of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setModel(new_model)
        self.__car_repository.addCar(self.__car)

    def changePriceRange(self, new_price_range):
        """
        Changes the price range of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setPriceRange(new_price_range)
        self.__car_repository.addCar(self.__car)
    
    def changeManufacturer(self, new_manufacturer):
        """
        Changes the manufacturer of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setManufacturer(new_manufacturer)
        self.__car_repository.addCar(self.__car)
    
    def changeColor(self, new_color):
        """
        Changes the color of a car
        """
        self.__car_repository.deleteCar(self.__car.getPlateNumber())
        self.__car.setColor(new_color)
        self.__car_repository.addCar(self.__car)
