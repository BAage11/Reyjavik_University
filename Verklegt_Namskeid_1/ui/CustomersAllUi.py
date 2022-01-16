import os
from services.CustomerAllServices import CustomerAllServices
from ui.CustomerSpecificUi import CustomerSpecificUi
class CustomersAllUi():
    def __init__(self):
        self.__all_cust_services = CustomerAllServices()
        self.__customers = self.__all_cust_services.getCustomers()

    def printInformation(self):
        """
        Prints out all the customers and their information
        """
        os.system('cls')
        for customer in self.__customers:
            print("{} {}".format(str(customer + ":"), 
                                    self.__customers[customer].getName()))
        self.selectSpecificCustomer()
        return None

    def selectSpecificCustomer(self):
        """
        Gets the input from the user, the user inputs 0 if he wants to quit
        or inputs the ssn of a customer to select him
        """
        print("Veldu notanda til að fá nánari upplýsingar um")
        print("stimplaðu inn kennitölu til að velja viðskiptavin")
        print("0. Til að hætta")
        choice = input("> ")
        self.__all_cust_services.createValidChoices()
        while self.__all_cust_services.isValidChoice(choice) == False:
            print(choice,"Er ekki lögleg aðgerð, reyndu aftur")
            choice = input("> ")
        if choice == "0":
            return None # Þarf að fara yfir á main menu aftur
        else:
            specific_cust_ui = CustomerSpecificUi(choice) # Þarf að fara yfir á specific customer info
            specific_cust_ui.printInformation()