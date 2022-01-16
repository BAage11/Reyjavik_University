import os
from services.CarRentServices import CarRentServices
from ui.CustomerAddUi import CustomerAddUi
from services.CustomerSpecificServices import CustomerSpecificServices
from ui.CustomerSearchUi import CustomerSearchUi
from models.Car import Car
from ui.InsuranceUi import InsuranceUi
from ui.CarRentAgreementUi import CarRentAgreementUi
from ui.CarSearchUi import CarSearchUi
class CarRentUi():
    def __init__(self):
        self.__rent_services = CarRentServices()
        self.__search_customer_ui = CustomerSearchUi()
        self.__specific_customer_services = CustomerSpecificServices()

    def isNewCustomer(self):
        """
        Asks the user if its a new customer
        """
        os.system('cls')
        print ("-------- Bókunarferli 1 af 5 ---------")
        print ("---- Er þetta nýr viðskiptavinur? ----")
        print ("1. Já")
        print ("2. Nei")
        print ("3. Til baka")
        self.executeChoice(self.getChoice())

    def bookingProcess(self, customer):
        """
        Booking proccess after selecting customer
        """
        print("-------- Bókunarferli 3 af 5 ---------")
        search_car = CarSearchUi()
        from_date, return_date, car = search_car.searchCarMenu()
        print("-------- Bókunarferli 4 af 5 ---------")
        insurance = InsuranceUi().AddInsuranceMenu()
        print("-------- Bókunarferli 5 af 5 ---------")
        rent_agreement = CarRentAgreementUi(customer, car, from_date, return_date, insurance)
        rent_agreement.printReceipt()

    def getChoice(self):
        """
        Gets the choice from the user
        """
        print("Veldu aðgerð")
        choice = input("> ")
        while self.__rent_services.isValidChoice(choice) == False:
            print(choice,"Er ekki lögleg aðgerð, reyndu aftur")
            choice = input("> ")
        return choice

    def executeChoice(self, choice):
        """
        Executes the choice the user chose
        """
        if choice == "1":
            print("-------- Bókunarferli 2 af 5 ---------")
            customer = CustomerAddUi().addUserMenu()
            self.bookingProcess(customer)
        elif choice == "2":
            print("-------- Bókunarferli 2 af 5 ---------")
            ssn = self.__search_customer_ui.getSsn()
            customer = self.__specific_customer_services.getCustomer(ssn)
            self.bookingProcess(customer)
        elif choice == "3":
            print ("Til baka")
