from models.Customer import Customer
from repositories.CustomerRepository import CustomerRepository
class CustomerAddServices():
    def __init__(self):
        self.__customerRepo = CustomerRepository()

    def isValidName(self, full_name):
        """
            This method checks to see if the name of a new user is
            valid and returns true if it is. it returns false otherwise
            For a name to be valid it has to only contain characters
            that ar in the alphabet, there can be no numbers or special
            characters.
        """
        all_names = full_name.strip().split()
        for name in all_names:
            if not name.isalpha():
                return False
        return True
    
    def isValidSsn(self, ssn):
        """
            A ssn is valid if the first two digits are <= 31 and > 0,
            if the second two digits are <= 12 and > 0 and the third
            pair of digits have to be > 0 and <= 99. the fourht pair of 
            digits have to be >= 20 and <= 99. The second to last number
            should follow the checksum equation and the last number should
            be the century the person was born in(either 9 or 0)
            a ssn is also always 10digits long

            the checksum equation is
            C = 11 - ((3xD1 + 2xD2 + 7xM1 + 6xM2 + 5xY1 + 4xY2 + 3xR1 + 2xR2) mod 11) 
            D = day, M = Month, Y = year, R = random
        """
        if not (len(ssn) == 10 and ssn.isdigit()):
            return False
        if not ssn[-1] == "9" and not ssn[-1] == "0":
            return False
        if 0 >= int(ssn[0:2]) or int(ssn[0:2]) > 31:
            return False 
        if 0 >= int(ssn[2:4]) or int(ssn[2:4]) > 12:
            return False
        if int(ssn[6:8]) < 20:
            return False
        d1 = int(ssn[0])
        d2 = int(ssn[1])
        m1 = int(ssn[2])
        m2 = int(ssn[3])
        y1 = int(ssn[4])
        y2 = int(ssn[5])
        r1 = int(ssn[6])
        r2 = int(ssn[7])
        checksum = 11-((3*d1 + 2*d2 + 7*m1 + 6*m2 + 5*y1 + 4*y2 + 3*r1 + 2*r2) % 11)
        if not int(ssn[8]) == checksum:
            return False
        if ssn in self.__customerRepo.getCustomers():
            return False
        return True
    
    def isValidAddress(self, address):
        """
        A address is valid if it contains a word that contains 
        only alphabetic letters and then space and after the space
        there is a number
        """
        address = address.split()
        if not len(address)  == 2:
            return False
        if not address[0].isalpha():
            return False
        if not address[1].isdigit():
            return False
        return True
    
    def isValidPhone(self, phone_nr):
        """ 
        A valid phone number is just a string that contains
        7 digits and nothing else
        """
        if not len(phone_nr) == 7:
            return False
        if not phone_nr.isdigit():
            return False
        return True

    def isValidNationality(self, nationality):
        """ 
        A valid nationality is a string that contains one name
        and the name can not contain digits or special characters
        """
        nationality = nationality.strip().split()
        if len(nationality) > 1:
            return False
        if not nationality[0].isalpha():
            return False
        return True 

    def addCustomer(self, name, ssn, home_address, phone_nr, country):
        """
        Adds customer to customer repo
        """
        new_customer = Customer(name, ssn, home_address, phone_nr, country)
        self.__customerRepo.addCustomer(new_customer)







