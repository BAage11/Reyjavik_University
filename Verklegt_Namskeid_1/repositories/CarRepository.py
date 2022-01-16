import csv
from models.Car import Car
class CarRepository():
    def __init__(self):
        """
        Creates and empty dictonary for the cars
        """
        self.__cars = {}

    def getCars(self):
        """
        Fetches the data from Cars.csv and stores it in the car
        dictonary that __init__() created
        """
        with open("./database/Cars.csv", "r", encoding="utf-8-sig") as cars_database:
            csv_reader = csv.DictReader(cars_database)
            for line in csv_reader:
                plate_number = line["plate_number"]
                status = line["status"]
                car_type = line["car_type"]
                seats = line["seats"]
                fuel_type = line["fuel_type"]
                model = line["model"]
                price_range = line["price_range"]
                manufacturer = line["manufacturer"]
                color = line["color"]
                self.__cars[plate_number] = Car(plate_number, status, car_type,
                                                seats, fuel_type, model,
                                                price_range, manufacturer, color)
        return self.__cars

    def addCar(self, car):
        """
        Adds a car to the Cars.csv file
        """
        self.getCars()
        self.__cars[car.getPlateNumber()] = car
        with open("./database/Cars.csv", "a+", encoding="utf-8") as cars_database:
            cars_database.write(car.__repr__() + "\n")
        return None

    def deleteCar(self, car_number_plate):
        """
        Deletes a car from the system
        """
        if str(car_number_plate) in self.__cars:
            self.__cars.pop(str(car_number_plate))
            with open("./database/Cars.csv", "w", encoding="utf-8") as cars_database:
                cars_database.write("plate_number,status,car_type,seats,"
                                    "fuel_type,model,price_range,manufacturer,"
                                    "color\n")
                for car in self.__cars:
                    cars_database.write(self.__cars[car].__repr__() + "\n")
        return None