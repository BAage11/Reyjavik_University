import os
from services.CustomerSearchServices import CustomerSearchServices
from ui.CustomerSpecificUi import CustomerSpecificUi
class CustomerSearchUi():
    def __init__(self):
        self.__search_services = CustomerSearchServices()
        self.__name = ""
        self.__ssn = ""

    def searchUserMenu(self):
        """
        Prints out the menu
        """
        os.system('cls')
        print("-------- Leita að Viðskiptavin --------")
        print("0. Til að fara til baka")
        self.openCustomerInfo(self.getSsn())
        print("---------------------------------------")

    def getSsn(self):
        """
        Gets the user to input a SSN
        """
        ssn = input("{:<15}".format("Kennitala viðskiptavinar: "))
        while self.__search_services.isValidSsn(ssn) == False:
            if ssn == "0":
                return 0
            print("Enginn viðskiptavinur með þessa kennitölu")
            ssn = input("{:<15}".format("Kennitala viðskiptavinar: "))
        return ssn
    
    def openCustomerInfo(self, ssn):
        """
        If the user inputs a correct ssn prints out the customer information
        """
        if ssn:
            customer_specif = CustomerSpecificUi(ssn)
            customer_specif.printInformation()
        return None
