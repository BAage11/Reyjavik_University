import csv
from models.CreditCard import CreditCard
class CreditCardRepository():
    def __init__(self):
        self.__cards = {}

    def getCards(self):
        """
        Gets all the credit cards
        """
        with open("./database/CreditCards.csv", "r", encoding="utf-8-sig") as card_database:
            csv_reader = csv.DictReader(card_database)
            for line in csv_reader:
                customer_ssn = line["customer_ssn"]
                credit_card_number = line["credit_card_number"]
                exp_date = line["expiration_date"]
                cvc = line["cvc"]
                self.__cards[customer_ssn] = CreditCard(customer_ssn,credit_card_number,exp_date, cvc)
        return self.__cards

    def addCard(self, card):
        """
        Adds a card to the CreditCards.csv file
        """
        with open("./database/CreditCards.csv", "a+", encoding="utf-8") as card_database:
            card_database.write(card.__repr__() + "\n")
        return None
