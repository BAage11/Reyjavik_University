from models.Person import Person
class Employee(Person):
    """
    Class to access, or to create an instance of an employee for the car rental
    This class is a subclass, and inheritates information (name and ssn) 
    from the superclass Person
    """
    def __init__(self, name, ssn, employee_id, password):
        Person.__init__(self, name, ssn)
        self.__id = employee_id
        self.__password = password
    
    def setId(self, new_id):
        """
        Sets the id to a new value
        """
        self.__id = new_id

    def setPassword(self, password):
        """
        Sets the password to a new value
        """
        self.__password = password
    
    def getId(self):
        """
        Returns the id
        """
        return self.__id

    def getPassword(self):
        """
        Returns the password
        """
        return self.__password

    def login(self, number, password):
        """
        If the number and password match the password and id the user logs in
        """
        return number == self.getId() and password == self.getPassword()
    
    def __repr__(self):
        """
        Prints out all the variables with commas between
        """
        return "{},{},{},{}".format(self.getId(), self.getSsn(), 
                                    self.getName(), self.getPassword())
                                
    def __str__(self):
        """
        Prints out a menu of all the variables
        """
        return "{:<15}{}\n{:<15}{}\n{:<15}{}".format("Employee id:", self.getId(),
                                                     "SSN:", self.getSsn(),
                                                     "Name:", self.getName())
