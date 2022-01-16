from repositories.CustomerRepository import CustomerRepository
class CustomerAllServices():
    def __init__(self):
        self.__customer_repository = CustomerRepository()
        self.__customers = self.__customer_repository.getCustomers()
        self.__valid_choices = ["0"]

    def getCustomers(self):
        """
        returns all customers
        """
        self.__customers = self.__customer_repository.getCustomers()
        return self.__customers

    def createValidChoices(self):
        """
        Creates all valid choices
        """
        for customer_ssn in self.getCustomers():
            self.__valid_choices.append(customer_ssn)
        return None
    
    def isValidChoice(self, choice):
        """
        Checks if the users choice is valid
        """
        return choice in self.__valid_choices
    
    