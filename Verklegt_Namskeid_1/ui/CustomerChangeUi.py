import os
from services.CustomerChangeServices import CustomerChangeServices
from services.CustomerAddServices import CustomerAddServices
from services.CarRegisterService import CarRegisterService
class CustomerChangeUi():
    def __init__(self):
        self.__customer_services = CustomerChangeServices()
        self.__customer_register_services = CustomerAddServices()
        self.__car_register_services = CarRegisterService()
        self.__save = True

    def customerRegisterChangeMainUi(self, ssn):
        """
        Prints out the customer change main menu
        """
        self.__customer = self.__customer_services.getCustomer(ssn)
        os.system('cls')
        while self.__save:
            print("---------- Breyta Viðskiptavin ---------")
            print("1. " + ssn)
            print("2. " + self.__customer.getName())
            print("3. " + self.__customer.getAddress())
            print("4. " + self.__customer.getPhone())
            print("5. " + self.__customer.getCountry())
            print("6. Vista")
            print("-------------------------------")
            print("Hverju viltu breyta?(veldu 1 - 6)")
            self.executeChoice(self.getChoice())

    def getChoice(self):
        """
        Gets what the user inputs as his choice
        """
        choice = input("> ")
        while not self.__customer_services.isValidChoice(choice):
            print(choice, "Er ekki lögleg aðgerð")
            choice = input("> ")
        return choice

    def executeChoice(self, choice):
        """
        Executes the users choice
        """ 
        if choice == "1":
            new_value = self.getSsn()
            self.__customer_services.changeSsn(new_value)
        elif choice == "2":
            new_value = self.getName()
            self.__customer_services.changeName(new_value)
        elif choice == "3":
            new_value = self.getAddress()
            self.__customer_services.changeAddress(new_value)
        elif choice == "4":
            new_value = self.getPhone()
            self.__customer_services.changePhone(new_value)
        elif choice == "5":
            new_value = self.getCountry()
            self.__customer_services.changeCountry(new_value)
        elif choice == "6":
            self.__save = False
            return None

    def getSsn(self):
        """
        The user inputs a social security number
        """
        ssn = input("{:<15}".format("Kennitala:"))
        while self.__car_register_services.isValidPlateNumber(ssn) == False:
            print("Þetta er ekki löglegt kennitala!")
            ssn = input("{:<15}".format("Kennitala:"))
        return ssn

    def getName(self):
        """
        The user inputs a name
        """
        name = input("{:<15}".format("Nafn:"))
        while self.__customer_register_services.isValidName(name) == False:
            print("Þetta er ekki löglegt nafn!")
            name = input("{:<15}".format("Nafn:"))
        return name

    def getAddress(self):
        """
        The user inputs an address
        """
        address = input("{:<15}".format("Heimilisfang:"))
        while self.__customer_register_services.isValidAddress(address) == False:
            print("Þetta er ekki löglegt heimilisfang!")
            address = input("{:<15}".format("Heimilisfang:"))
        return address

    def getPhone(self):
        """
        The user inputs a phone number
        """
        phone = input("{:<15}".format("Símanúmer:"))
        while self.__customer_register_services.isValidPhone(phone) == False:
            print("Þetta er ekki löglegt símanúmer!")
            phone = input("{:<15}".format("Símanúmer:"))
        return phone

    def getCountry(self):
        """
        The user inputs a country
        """
        country = input("{:<15}".format("Land:"))
        while self.__customer_register_services.isValidNationality(country) == False:
            print("Þetta er ekki löglegt land!")
            country = input("{:<15}".format("Land:"))
        return country
