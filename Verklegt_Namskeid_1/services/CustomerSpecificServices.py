from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository
from repositories.EmployeeRepository import EmployeeRepository
class CustomerSpecificServices():
    def __init__(self):
        self.__customer_repository = CustomerRepository()
        self.__order_repository = OrderRepository()
        self.__employee_repository = EmployeeRepository()
        self.__customers = self.__customer_repository.getCustomers()
        self.__orders = self.__order_repository.getOrders()
        self.__order_choices = []

    def getCustomer(self, ssn):
        """
        Locates the customer based on given social security number (ssn)
        to find all the orders of the customer
        """
        self.__customers = self.__customer_repository.getCustomers()
        return self.__customers[ssn]
    
    
    def findOrders(self, ssn):
        """ 
        Finds all the orders for the given customer ssn,
        and retrives the order which the user would like to find
        """
        self.__customer_orders = []
        orders = self.__order_repository.getOrders()
        for order in orders:
            if orders[order].getCustomerId() == ssn:
                self.__customer_orders.append(orders[order])
        return self.__customer_orders

    def isValidChoices(self, choice):
        """
        Checks if the choice is valid
        """
        valid_choices = ['1', '2', '3', '4', '5', '6', '7']
        return choice in valid_choices

    def isValidChoice(self, choice):
        """
        Checks if the choice is valid
        """
        choices = ["j", "n"]
        return choice in choices
    
    def deleteCust(self, ssn):
        """
        Delets a customer
        """
        self.__customer_repository.deleteCustomer(ssn)
        self.deleteAllOrders(ssn)
    
    def deleteAllOrders(self, ssn):
        """
        Deletes all the orders the customer had
        """
        
        orders = self.findOrders(ssn)
        for order in orders:
            self.__order_repository.deleteOrder(order.getOrderId())
        return None
            
    
    def validOrder(self, ssn, num):
        """
        Checks if order is valid by checking the length of the order list
        """
        orders = self.findOrders(ssn)
        if int(num) >= 1 and int(num) < len(self.findOrders(ssn))+1:
            return True
        return False

    def cancelOrder(self, num, orders):
        """
        Selects the order and deletes it
        """
        order_to_delete = orders[num]
        self.__order_repository.deleteOrder(order_to_delete.getOrderId())
        return None

    def getOrder(self, order_nr):
        """
        Returns specific order
        """
        self.__specific_order = self.__customer_orders[int(order_nr)-1]
        return self.__specific_order

    def checkOrders(self, orders):
        """
        Checks if the customer has any orders
        """
        if len(orders) != 0:
            return True
        return False

    def changePlateNumber(self, new_plate_number):
        """
        Changes the plate number of an order
        """
        self.__order_repository.deleteOrder(self.__specific_order.getOrderId())
        self.__specific_order.setCarPlate(new_plate_number)
        self.__order_repository.addOrder(self.__specific_order)

    def changeOrderSsn(self, new_ssn):
        """
        Changes the ssn of an order
        """
        self.__order_repository.deleteOrder(self.__specific_order.getOrderId())
        self.__specific_order.setCustomer(new_ssn)
        self.__order_repository.addOrder(self.__specific_order)

    def changePickUpDate(self, new_pick_up_date):
        """
        Changes the pick up date of an order
        """
        self.__order_repository.deleteOrder(self.__specific_order.getOrderId())
        self.__specific_order.setRentedDate(new_pick_up_date)
        self.__order_repository.addOrder(self.__specific_order)

    def changeReturnDate(self, new_return_date):
        """
        Changes the return date of an order
        """
        self.__order_repository.deleteOrder(self.__specific_order.getOrderId())
        self.__specific_order.setReturnDate(new_return_date)
        self.__order_repository.addOrder(self.__specific_order)

    def changePrice(self, new_price):
        """
        Changes the price of an order
        """
        self.__order_repository.deleteOrder(self.__specific_order.getOrderId())
        self.__specific_order.setCost(new_price)
        self.__order_repository.addOrder(self.__specific_order)

    def changeInsurancePrice(self, new_insurance_price):
        """
        Changes the insurance of an order
        """
        self.__order_repository.deleteOrder(self.__specific_order.getOrderId())
        self.__specific_order.setInsurance(new_insurance_price)
        self.__order_repository.addOrder(self.__specific_order)

    def changeEmployeeNr(self, new_employee_nr):
        """
        Changes the employee number of an order
        """
        self.__order_repository.deleteOrder(self.__specific_order.getOrderId())
        self.__specific_order.setEmployee(new_employee_nr)
        self.__order_repository.addOrder(self.__specific_order)

    def isValidPrice(self, price):
        """
        Checks if the price is valid
        """
        return price.isdigit()

    def isValidEmployee(self, employee_nr):
        """
        Checks if the employee number is valid
        """
        employees = self.__employee_repository.getEmployees()
        if employee_nr in employees:
            return True
        return False