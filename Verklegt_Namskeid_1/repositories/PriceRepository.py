import csv
from models.Order import Order


class PriceRepository():
    def __init__(self):
        """
        Creates an empty dictonary for the orders
        """
        self.__orders = {}

    def getPrices(self):
        """
        Fetches the data from Orders.csv and stores it in the orders
        dictonary that __init__() created
        """
        with open("./database/Prices.csv", "r", encoding="utf-8-sig") as price_database:
            csv_reader = csv.DictReader(price_database)
            for line in csv_reader:
                order_id = line["order_id"]
                care_plate = line["car_plate"]
                customer_ssn = line["customer_ssn"]
                pick_up_date = line["pick_up_date"]
                return_date = line["return_date"]
                cost = line["cost"]
                insurance = line["insurance"]
                self.__orders[order_id] = Order(order_id, care_plate, customer_ssn,
                                                pick_up_date, return_date, cost, insurance)
        return self.__orders