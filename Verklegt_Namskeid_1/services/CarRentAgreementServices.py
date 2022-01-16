from datetime import datetime
from models.Order import Order
from models.CreditCard import CreditCard
from repositories.OrderRepository import OrderRepository
from repositories.CreditCardRepository import CreditCardRepository
class CarRentAgreementServices():
    def __init__(self):
        self.__valid_choices = ["1", "2", "3", "4"]
        self.__order_repo = OrderRepository()

    def isValidChoice(self, choice):
        """
        checks if the users choice is valid
        """
        return choice in self.__valid_choices

    def calculatePrice(self, car, insurance, total_days):
        """
        Calculates the price
        """
        car_price_unstripped = car.getPriceRange()
        car_price = int(car_price_unstripped.replace(".", ""))
        total_price = car_price * total_days.days + insurance
        return total_price

    def getOrderId(self):
        """
        Gets the next order id
        """
        orders = self.__order_repo.getOrders()
        order_id = 0
        for order in orders:
            if int(order_id) < int(orders[order].getOrderId()):
                order_id = orders[order].getOrderId()
        return int(order_id) + 1
    
    def confirmOrder(self, customer, car, from_date, return_date, insurance):
        """
        Confirms and creates the order
        """
        order_id = self.getOrderId()
        car_plate = car.getPlateNumber()
        customer_id = customer.getSsn()
        rented = from_date
        returned = return_date
        cost = self.calculatePrice(car, insurance, returned - rented)
        order = Order(order_id, car_plate, customer_id, rented,
                    returned, cost, insurance)
        self.__order_repo.addOrder(order)
    
    def isValidPayChoice(self, choice):
        """
        Checks if the pay choice is valid
        """
        return choice == "j" or choice == "n"

    def isValidCardNumber(self, number):
        """
        Checks if the card number is valid
        """
        return number.isdigit() and len(number) == 16
    
    def isValidExpDate(self, date):
        """
        Checks if the exp date is valid
        """
        try:
            year = int(date[:4])
            month = int(date[5:])
            return len(date) == 7 and date[4] == "-"
        except:
            return False
        
    def isValidCvc(self, cvc):
        """
        Checks if the cvc is valid
        """
        return len(cvc) == 3 and cvc.isdigit()
    
    def addCard(self, card_info, ssn, choice):
        """
        Adds the card to card.csv
        """
        card_nr, exp_date, cvc = card_info.split(":")
        card = CreditCard(ssn, card_nr, exp_date, cvc, choice)
        repo = CreditCardRepository()
        repo.addCard(card)
        
