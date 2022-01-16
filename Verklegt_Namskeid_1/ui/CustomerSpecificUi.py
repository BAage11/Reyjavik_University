import os
from services.CustomerSpecificServices import CustomerSpecificServices
from ui.CustomerChangeUi import CustomerChangeUi
from ui.CarRegisterUi import CarRegisterUi
from services.CustomerSearchServices import CustomerSearchServices
from ui.CarSearchUi import CarSearchUi

class CustomerSpecificUi():
    def __init__(self, ssn):
        self.__specific_cust_services = CustomerSpecificServices()
        self.__customer = self.__specific_cust_services.getCustomer(ssn)
        self.__cust_change = CustomerChangeUi()
        self.__cust_search_services = CustomerSearchServices()
        self.__car_search = CarSearchUi()
        self.__car_register_ui = CarRegisterUi()
        self.__save = True

    def printInformation(self):
        """
        Prints out all the information
        """
        os.system('cls')
        print("------------- {} -------------".format(self.__customer.getName()))
        print(self.__customer)
        orders = self.__specific_cust_services.findOrders(self.__customer.getSsn())
        for i in range(len(orders)):
            print("---------- Pöntun {} ----------".format(i+1))
            print(str(orders[i]))
            print("------------------------------")
        
        if self.likeToDelete():
            self.__specific_cust_services.deleteCust(self.__customer.getSsn())
            print("Notandanum Hefur verið eytt úr kerfinu!")
            return None
        if self.likeTochange():
            self.__cust_change.customerRegisterChangeMainUi(self.__customer.getSsn())
        if self.likeTochangeOrders():
            self.__selected_order_to_change = self.selectOrderToChange()
            self.orderChangeMainUi(self.__selected_order_to_change)
            print("Pöntun hefur verið breytt")
        if self.__specific_cust_services.checkOrders(orders):
            if self.likeToCancelOrder():
                self.__selected_order = self.selectOrder()
                self.__specific_cust_services.cancelOrder(int(self.__selected_order) - 1, orders)
                print("Pöntun hefur verið afpöntuð")
        print("Ýttu á enter til að halda áfram")
        input("")
        return None

    def likeToDelete(self):
        """
        The user inputs whether he wants to delete a customer
        """
        print("Langar þér að EYÐA notandandanum? (j/n)")
        choice = input("> ").strip().lower()
        while self.__specific_cust_services.isValidChoice(choice) == False:
            print(choice, "er ekki lögleg aðgerð")
            choice = input("> ").strip().lower()
        if "j" == choice:
            return True
        return False

    def likeTochange(self):
        """
        The user inputs whether he wants to change information about the customer
        """
        print("Langar þér að breyta eitthverjum upplýsingum um notandann? (j/n)")
        choice = input("> ").strip().lower()
        while self.__specific_cust_services.isValidChoice(choice) == False:
            print(choice, "er ekki lögleg aðgerð")
            choice = input("> ").strip().lower()
        if "j" == choice:
            return True
        return False

    def likeTochangeOrders(self):
        """
        The user inputs whether he wants to change an order or not
        """
        print("Langar þér að breyta eitthverjum upplýsingum í pöntunum viðskiptavins? (j/n)")
        choice = input("> ").strip().lower()
        while self.__specific_cust_services.isValidChoice(choice) == False:
            print(choice, "er ekki lögleg aðgerð")
            choice = input("> ").strip().lower()
        if "j" == choice:
            return True
        return False
    
    def likeToCancelOrder(self):
        """
        The user inputs whether he wants to cancel an order or not
        """
        print("Langar þér að afpanta pöntun? (j/n)")
        choice = input("> ").strip().lower()
        while self.__specific_cust_services.isValidChoice(choice) == False:
            print(choice, "er ekki lögleg aðgerð")
            choice = input("> ").strip().lower()
        if "j" == choice:
            return True
        return False

    def selectOrderToChange(self):
        """
        The user selects an order to change
        """
        print("Veldu pöntun til að breyta.")
        choice = input("> ").strip()
        while self.__specific_cust_services.validOrder(self.__customer.getSsn(), choice) == False:
            choice = input("> ").strip()
        return choice

    def selectOrder(self):
        """
        The user selects an order to cancel
        """
        print("Veldu pöntun til að afpanta.")
        choice = input("> ").strip()
        while self.__specific_cust_services.validOrder(self.__customer.getSsn(), choice) == False:
            choice = input("> ").strip()
        return choice

    def orderChangeMainUi(self, order_nr):
        """
        Prints the menu for changing the order
        """
        self.__order = self.__specific_cust_services.getOrder(order_nr)
        os.system('cls')
        save = True
        while save:
            print("---------- Breyta Pöntun ---------")
            print("1. Bílnúmer: " + self.__order.getCarPlate())
            print("2. Kennitala: " + self.__order.getCustomerId())
            print("3. Leigudagur:" + self.__order.getRentedDate())
            print("4. Skiladagur: " + self.__order.getReturnDate())
            print("5. Kostnaður: " + self.__order.getCost())
            print("6. Kostnaður á tryggingum: " + self.__order.getInsurance())
            print("7. Vista")
            print("-------------------------------")
            print("Hverju viltu breyta?(veldu 1 - 7)")
            save = self.executeChoice(self.getChoice())

    def getChoice(self):
        """
        Gets what the user inputs as his choice
        """
        choice = input("> ")
        while not self.__specific_cust_services.isValidChoices(choice):
            print(choice, "Er ekki lögleg aðgerð")
            choice = input("> ")
        return choice

    def getCost(self):
        """
        The user inputs price
        """
        price = input("{:<15}".format("Kostnaður:"))
        while self.__specific_cust_services.isValidPrice(price) == False:
            print("Þetta er ekki löglegur kostnaður!")
            price = input("{:<15}".format("Kostnaður:"))
        return price

    def getSsn(self):
        """
        The user inputs a  social security number
        """
        ssn = input("{:<15}".format("Kennitala viðskiptavinar: "))
        while self.__cust_search_services.isValidSsn(ssn) == False:
            if ssn == "0":
                return 0
            print("Enginn viðskiptavinur með þessa kennitölu")
            ssn = input("{:<15}".format("Kennitala viðskiptavinar: "))
        return ssn

    def executeChoice(self, choice):
        """
        Executes the users choice
        """ 
        if choice == "1":
            new_value = self.__car_register_ui.getPlateNumber()
            self.__specific_cust_services.changePlateNumber(new_value)
        elif choice == "2":
            new_value = self.getSsn()
            self.__specific_cust_services.changeOrderSsn(new_value)
        elif choice == "3":
            new_value = self.__car_search.getDate()
            self.__specific_cust_services.changePickUpDate(new_value)
        elif choice == "4":
            new_value = self.__car_search.getDate()
            self.__specific_cust_services.changeReturnDate(new_value)
        elif choice == "5":
            new_value = self.getCost()
            self.__specific_cust_services.changePrice(new_value)
        elif choice == "6":
            new_value = self.getCost()
            self.__specific_cust_services.changeInsurancePrice(new_value)
        elif choice == "7":
            return False
        return True
