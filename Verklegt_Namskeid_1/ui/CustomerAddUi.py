import os
from services.CustomerAddServices import CustomerAddServices
from models.Customer import Customer
class CustomerAddUi():
    def __init__(self):
        self.__userService = CustomerAddServices()
        self.__name = ""
        self.__ssn = ""
        self.__address = ""
        self.__phone = ""
        self.__nationality = ""

    def addUserMenu(self):
        """
        The user adds a customer by inputting the neccesary information
        """
        os.system('cls')
        print("--- Skrá Nýjan Viðskiptavin ---")
        self.__name = self.getName()
        self.__ssn = self.getSsn()
        self.__address = self.getAddress()
        self.__phone = self.getPhone()
        self.__nationality = self.getNationality()
        print("-------------------------------")
        self.__userService.addCustomer(self.__name, self.__ssn,
                                       self.__address, self.__phone,
                                       self.__nationality)
        print("VIÐSKIPTAVINI HEFUR VERIÐ BÆTT VIÐ")
        print("Til að halda áfram ýttu á enter")
        input("")
        return Customer(self.__name, self.__ssn, self.__address, self.__phone, self.__nationality)
    
    def getName(self):
        """
        The user inputs a name
        """
        name = input("{:<15}".format("Nafn:"))
        while self.__userService.isValidName(name) == False:
            print("Þetta er ekki löglegt nafn!")
            name = input("{:<15}".format("Nafn:"))
        return name
    
    def getSsn(self):
        """
        The user inputs a social security number
        """
        ssn = input("{:<15}".format("Kennitala:"))
        while self.__userService.isValidSsn(ssn) == False:
            print("Þetta er ekki lögleg kennitala!")
            ssn = input("{:<15}".format("Kennitala:"))
        return ssn
    
    def getAddress(self):
        """
        The user inputs an address
        """
        address = input("{:<15}".format("Heimilisfang:"))
        while self.__userService.isValidAddress(address) == False:
            print("Þetta er ekki löglegt heimilisfang!")
            address = input("{:<15}".format("Heimilisfang:"))
        return address
    
    def getPhone(self):
        """
        The user inputs a phone number
        """
        phone = input("{:<15}".format("Símanúmer:"))
        while self.__userService.isValidPhone(phone) == False:
            print("Þetta er ekki löglegt símanúmer!")
            phone = input("{:<15}".format("Símanúmer:"))
        return phone
    
    def getNationality(self):
        """
        The user inputs a nationality
        """
        nationality = input("{:<15}".format("Land:"))
        while self.__userService.isValidNationality(nationality) == False:
            print("Þetta er ekki löglegt land!")
            nationality = input("{:<15}".format("Land:"))
        return nationality

