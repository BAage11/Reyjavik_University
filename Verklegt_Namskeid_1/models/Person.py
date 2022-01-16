class Person():
    """
    Superclass for the subclasses 'Employee' and 'Customer'
    for creating (and retreiving) the name and social security number (ssn) 
    for individuals (employees and customers)
    """
    def __init__(self, name, ssn):
        self.__name = name
        self.__ssn = ssn
    
    def setName(self, new_name):
        """
        Sets the name to a new value
        """
        self.__name = new_name

    def setSsn(self, new_ssn):
        """
        Sets the ssn to a new value
        """
        self.__ssn = new_ssn

    def getName(self):
        """
        Returns the name
        """
        return self.__name

    def getSsn(self):
        """
        Returns the ssn
        """
        return self.__ssn

    def __repr__(self):
        """
        Prints out all the variables with commas between
        """
        return "{},{}".format(self.getSsn(), self.getName())

    def __str__(self):
        """
        Prints out a menu of all the variables
        """
        return "{:<15}{}\n{:<15}{}".format("SSN:", self.getSsn(), 
                                           "Name:", self.getName())
