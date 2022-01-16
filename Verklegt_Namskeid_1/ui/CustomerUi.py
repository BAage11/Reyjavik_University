import os
from services.CustomerMenuServices import CustomerMenuServices
from ui.CustomerAddUi import CustomerAddUi
from ui.CustomerSearchUi import CustomerSearchUi
from ui.CustomersAllUi import CustomersAllUi
class CustomerUi():
    def __init__(self):
        self.__customer_menu_services = CustomerMenuServices()
        self.__cust_add = CustomerAddUi()
        self.__cust_search = CustomerSearchUi()
    
    def customerMenu(self):
        """
        Prints out the menu 
        """
        os.system('cls')
        print("-------- Viðskiptavinir --------")
        print("1. Skrá nýjan viðskiptavin")
        print("2. Leita að viðskiptavin")
        print("3. Allir viðskiptavinir")
        print("4. Fara heim")
        print("--------------------------------")
        self.executeChoice(self.getChoice())
    
    def getChoice(self):
        """
        Gets the choice from the user
        """
        print("Veldu aðgerð")
        choice = input("> ")
        while self.__customer_menu_services.isValidChoice(choice) == False:
            print(choice,"Er ekki lögleg aðgerð, reyndu aftur")
            choice = input("> ")
        return choice

    def executeChoice(self, choice):
        """
        Executes the choice the user chose
        """
        if choice == "1":
            self.__cust_add.addUserMenu()
        elif choice == "2":
            self.__cust_search.searchUserMenu()
        elif choice == "3":
            cust_all = CustomersAllUi()
            cust_all.printInformation()
        return None

        