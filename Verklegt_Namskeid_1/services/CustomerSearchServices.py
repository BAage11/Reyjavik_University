from models.Customer import Customer
from repositories.CustomerRepository import CustomerRepository
class CustomerSearchServices():
    """
    Check to see if the written ssn by the user is valid or not 
    (customer found in the database)
    """
    def __init__(self):
        self.__customerRepo = CustomerRepository()

    def isValidSsn(self, ssn):
        """
        Checks if the ssn is valid
        """
        customers = self.__customerRepo.getCustomers()
        if ssn in customers:
            return True
        return False
        
        
