import os
import datetime
from services.CarRentAgreementServices import CarRentAgreementServices
from services.CustomerSpecificServices import CustomerSpecificServices
from ui.CustomerSearchUi import CustomerSearchUi
from ui.CarSearchUi import CarSearchUi
from models.Customer import Customer
from models.Car import Car
from models.Order import Order
class CarRentAgreementUi():
    def __init__(self, customer, car, from_date, return_date, insurance):
        self.__rent_agreement_services = CarRentAgreementServices()
        self.__specific_customer_services = CustomerSpecificServices()
        self.__car = car
        self.__customer = customer
        self.__cust_search = CustomerSearchUi()
        self.__pick_up_date = datetime.datetime.strptime(
                                    from_date, "%Y-%m-%d").date()
        self.__return_date = datetime.datetime.strptime(
                                    return_date, "%Y-%m-%d").date()
        self.__total_days = self.__return_date - self.__pick_up_date
        self.__insurance = insurance

    def theText(self):
        """
        The text for the receipt
        """
        print("----------- Leigusamningur -----------")
        print("-------- Viðskiptavinur --------")
        print(self.__customer)
        print("--------------------------------")
        print("-------------- Bíll ------------")
        print (self.__car)
        print("-------------------------------")
        print("------------- Verð ------------")
        print("{:<15}{}".format("Frá:", self.__pick_up_date))
        print("{:<15}{}".format("Til:", self.__return_date))
        print("{:<15}{}".format("Fjöldi daga:", self.__total_days.days))
        print("{:<15}{}".format("Kostnaður bíls:", int(self.__car.getPriceRange()) * int(self.__total_days.days)))
        print("{:<15}{}".format("Tryggingar:", self.__insurance))
        print("{:<15}{}".format("Samtals:", self.__rent_agreement_services.calculatePrice(self.__car,
                                                                                          self.__insurance,
                                                                                          self.__total_days)))
        print("-------------------------------")

    def printReceipt(self):
        """
        Prints the receipt
        """
        os.system('cls')
        self.theText()
        self.changeReceipt()

    def changeReceipt(self):
        """
        Asks if the user wants to change anything
        """
        choice = True
        while choice:
            print ("Eru einhverjar upplýsingar sem þarfnast breytingar?")
            print ("1. Viðskiptavinur")
            print ("2. Bíll")
            print ("3. Hætta við")
            print ("Ef engar upplýsingar þarfnast breytingar")
            print ("4. Staðfesta")
            print("-------------------------------")
            choice = self.executeChoice(self.getChoice())
            if choice == "q":
                return None
            self.theText()
        self.payWithWhat()
        print("PÖNTUN LOKIÐ!!")
        print("Ýttu á enter til að halda áfram")
        input("")

    def payWithWhat(self):
        """
        Asks the user how he wants to pay
        """
        print("Villtu greiða með reiðufé? (j/n)")
        choice = self.getPayChoice()
        if choice == "j":
            choice = "Greitt"
        card_info = self.getCardInfo()
        self.__rent_agreement_services.addCard(card_info, self.__customer.getSsn(), choice)

    def getCardInfo(self):
        """
        Gets all the card info
        """
        card_num = self.getCardNumber()
        card_exp_date = self.getExpiration()
        card_cvc = self.getCvc()
        return card_num + ":" + card_exp_date + ":" + card_cvc

    def getCvc(self):
        """
        Gets the CVC from the user
        """
        print("CVC kortsins:")
        cvc = input("> ")
        while self.__rent_agreement_services.isValidCvc(cvc) == False:
            print(cvc, "er ekki löglegt CVC")
            cvc = input("> ")
        return cvc

    def getCardNumber(self):
        """
        Gets the card number from the user
        """
        print("Kortanúmer viðskiptavinar")
        card_number = input("> ")
        while self.__rent_agreement_services.isValidCardNumber(card_number) == False:
            print(card_number, "er ekki löglegt kortanumer")
            card_number = input("> ")
        return card_number
    
    def getExpiration(self):
        """
        Gets the expiration date from the user
        """
        print("Fyrningardagsetning (yyyy-mm):")
        exp_date = input("> ")
        while self.__rent_agreement_services.isValidExpDate(exp_date) == False:
            print(exp_date, "er ekki lögleg fyrningardagsetning")
            exp_date = input("> ")
        return exp_date

    def getPayChoice(self):
        """
        Gets the payment choice from the user
        """
        choice = input("> ")
        while self.__rent_agreement_services.isValidPayChoice(choice) == False:
            print(choice, "er ekki lögleg aðgerð!")
            choice = input("> ")
        return choice


    def getChoice(self):
        """
        Gets the choice from the user
        """
        print("Veldu aðgerð")
        choice = input("> ")
        while self.__rent_agreement_services.isValidChoice(choice) == False:
            print(choice,"Er ekki lögleg aðgerð, reyndu aftur")
            choice = input("> ")
        return choice

    def executeChoice(self, choice):
        """
        Executes the choice the user chose
        """
        if choice == "1":
            print("breyta um Viðskiptavin")
            ssn = self.__cust_search.getSsn()
            self.__customer = self.__specific_customer_services.getCustomer(ssn)
            return True
        elif choice == "2":
            search_car = CarSearchUi()
            from_date, return_date, car = search_car.searchCarMenu()
            self.__pick_up_date = datetime.datetime.strptime(
                                    from_date, "%Y-%m-%d").date()
            self.__return_date = datetime.datetime.strptime(
                                    return_date, "%Y-%m-%d").date()
            self.__car = car
            return True
        elif choice == "3":
            return "q"
        elif choice == "4":
            self.__rent_agreement_services.confirmOrder(self.__customer, self.__car, 
                                                        self.__pick_up_date, self.__return_date, 
                                                        self.__insurance)
            print("--------------------------------------")
            return False