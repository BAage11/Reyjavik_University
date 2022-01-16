class Car():
    """
    Class who creates information about a new car,
    or delivers information about an existing car that has been
    put into the database 'Cars.csv'
    """
    def __init__(self, plate_number, status, car_type, seats, fuel_type,
                 model, price_range, manufacturer, color):
        self.__plate_number = plate_number 
        self.__status = status
        self.__car_type = car_type
        self.__seats = seats
        self.__fuel_type = fuel_type
        self.__model = model
        self.__price_range = price_range 
        self.__manufacturer = manufacturer
        self.__color = color

    def setPlateNumber(self, new_plate_number):
        """
        Sets the plate number to a new value
        """
        self.__plate_number = new_plate_number

    def setStatus(self, new_status):
        """
        Sets the status to a new value
        """
        self.__status = new_status

    def setCarType(self, new_car_type):
        """
        Sets the car type to a new value
        """
        self.__car_type = new_car_type

    def setSeats(self, new_seats):
        """
        Sets the number of seats to a new value
        """
        self.__seats = new_seats

    def setFuelType(self, new_fuel_type):
        """
        Sets the fuel type to a new value
        """
        self.__fuel_type = new_fuel_type

    def setModel(self, new_model):
        """
        Sets the model to a new value
        """
        self.__model = new_model

    def setPriceRange(self, new_price_range):
        """
        Sets the price range to a new value
        """
        self.__price_range = new_price_range

    def setManufacturer(self, new_manufacturer):
        """
        Sets the manufacturer to a new value
        """
        self.__manufacturer = new_manufacturer

    def setColor(self, new_color):
        """
        Sets the color to a new value
        """
        self.__color = new_color

    def getPlateNumber(self):
        """
        Returns the plate number
        """
        return self.__plate_number

    def getStatus(self):
        """
        Returns the status
        """
        return self.__status

    def getCarType(self):
        """
        Returns the car type
        """
        return self.__car_type

    def getSeats(self):
        """
        Returns the number of seats
        """
        return self.__seats

    def getFuelType(self):
        """
        Returns the fuel type
        """
        return self.__fuel_type

    def getModel(self):
        """
        Returns the model
        """
        return self.__model

    def getPriceRange(self):
        """
        Returns the price range
        """
        return self.__price_range

    def getManufacturer(self):
        """
        Returns the manufacturer
        """
        return self.__manufacturer

    def getColor(self):
        """
        Returns the color
        """
        return self.__color
    
    def __repr__(self):
        """
        Prints out all the variables with commas between
        """
        return "{},{},{},{},{},{},{},{},{}".format(self.getPlateNumber(), self.getStatus(), 
                                                   self.getCarType(), self.getSeats(),
                                                   self.getFuelType(), self.getModel(), 
                                                   self.getPriceRange(), self.getManufacturer(),
                                                   self.getColor())

    def __str__(self):
        """
        Prints out a menu of all the variables
        """
        return "{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}".format(
                                                   "Númeraplata:", self.getPlateNumber(), 
                                                   "Status bíls:", self.getStatus(), 
                                                   "Týpa:", self.getCarType(), 
                                                   "Fjöldi sæta:", self.getSeats(),
                                                   "Eldsneyti:", self.getFuelType(), 
                                                   "Árgerð:", self.getModel(),
                                                   "Framleiðandi:", self.getManufacturer(),
                                                   "Litur:", self.getColor(),
                                                   "Verðflokkur:", self.getPriceRange())
