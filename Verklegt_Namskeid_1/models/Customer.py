from models.Person import Person
class Customer(Person):
    """ 
    Class to create an instance of a customer (or access information about a registered customer), with his/her needed information to be kept in the database 'Customers.csv'
    This class is a subclass, and inheritates information (name and ssn) 
    from the superclass Person
    """
    def __init__(self, name, ssn, home_address, phone_number, country):
        Person.__init__(self, name, ssn)
        self.__home_address = home_address
        self.__phone_number = phone_number
        self.__country = country

    def setAddress(self, new_home_address):
        """
        Sets the address to a new value
        """
        self.__home_address = new_home_address

    def setPhone(self, new_phone_number):
        """
        Sets the phone to a new value
        """
        self.__phone_number = new_phone_number

    def setCountry(self, new_country):
        """
        Sets the country to a new value
        """
        self.__country = new_country

    def getAddress(self):
        """
        Returns the address
        """
        return self.__home_address

    def getPhone(self):
        """
        Returns the phone number
        """
        return self.__phone_number

    def getCountry(self):
        """
        Returns the country
        """
        return self.__country

    def __repr__(self):
        """
        Prints out all the variables with commas between
        """
        return "{},{},{},{},{}".format(self.getSsn(), self.getName(),
                                       self.getAddress(), self.getPhone(),
                                       self.getCountry())

    def __str__(self):
        """
        Prints out a menu of all the variables
        """
        return "{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}".format("Kennitala:", 
                                                                         self.getSsn(),
                                                                         "Nafn:", self.getName(),
                                                                         "Heimilisfang:", self.getAddress(),
                                                                         "Símanúmer:", self.getPhone(),
                                                                         "Land:", self.getCountry())
