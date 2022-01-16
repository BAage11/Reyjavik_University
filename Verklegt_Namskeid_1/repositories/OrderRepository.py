import csv
from models.Order import Order


class OrderRepository():
    def __init__(self):
        """
        Creates an empty dictonary for the orders
        """
        self.__orders = {}

    def getOrders(self):
        """
        Fetches the data from Orders.csv and stores it in the orders
        dictonary that __init__() created
        """
        with open("./database/Orders.csv", "r", encoding="utf-8-sig") as order_database:
            csv_reader = csv.DictReader(order_database)
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

    def addOrder(self, order):
        """
        Adds a car rental to the Orders.csv file
        """
        self.getOrders()
        self.__orders[order.getOrderId()] = order
        with open("./database/Orders.csv", "a+", encoding="utf-8") as order_database:
            order_database.write(order.__repr__() + "\n")
        return None

    def deleteOrder(self, order_id):
        """
        Deletes a order from the system
        """
        if str(order_id) in self.__orders:
            self.__orders.pop(str(order_id))
            with open("./database/Orders.csv", "w", encoding="utf-8") as order_database:
                order_database.write("order_id,car_plate,customer_ssn,pick_up_date,"
                                     "return_date,cost,insurance,employee_id\n")
                for order in self.__orders:
                    order_database.write(self.__orders[order].__repr__() + "\n")
        return None