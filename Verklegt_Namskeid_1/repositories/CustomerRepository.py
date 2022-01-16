import csv
from models.Customer import Customer

class CustomerRepository():
    def __init__(self): 
        """
        Creates and empty dictonary for the customers
        """
        self.__customers = {}
    
    def getCustomers(self):
        """
        Fetches the data from Customers.csv and stores it in the customer 
        dictonary that __init__() created
        """
        self.__customers = {}
        with open("./database/Customers.csv", "r", encoding="utf-8-sig") as customer_database:
            csv_reader = csv.DictReader(customer_database)
            for line in csv_reader:
                ssn = line["ssn"]
                name = line["name"]
                address = line["address"]
                phone = line["phone"]
                country = line["country"]
                self.__customers[ssn] = Customer(name, ssn, address, phone, country)
        return self.__customers

    def addCustomer(self, customer):
        """
        Adds a customer to the Customers.csv file
        """
        self.getCustomers()
        self.__customers[customer.getSsn()] = customer
        with open("./database/Customers.csv", "a+", encoding="utf-8") as customer_database:
            customer_database.write(customer.__repr__() + "\n")
        return None
    
    def deleteCustomer(self, customer_ssn):
        """
        Deletes a customer from the system
        """
        if str(customer_ssn) in self.__customers:
            self.__customers.pop(str(customer_ssn))     
            with open("./database/Customers.csv", "w", encoding="utf-8") as customer_database:
                customer_database.write("ssn,name,address,phone,country\n")
                for customer in self.__customers:
                    customer_database.write(self.__customers[customer].__repr__() + "\n")
        return None