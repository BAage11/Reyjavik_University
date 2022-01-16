class Order():
    """
    Class to create a new order, to be kept in the database 'Orders.csv'
    Also to be able to access data about an order already made in advance
    """
    def __init__(self,order_id, car_plate, customer_id, rented,
                 returned, cost, insurance):
        self.__order_id = order_id
        self.__car_plate = car_plate
        self.__customer_id = customer_id
        self.__rented_date = rented
        self.__return_date = returned
        self.__cost = cost
        self.__insurance = insurance
    
    def setOrderId(self, new_order_id):
        """
        Sets the order id to a new value
        """
        self.__order_id = new_order_id

    def setCarPlate(self, new_car):
        """
        Sets the car plate to a new value
        """
        self.__car_plate = new_car

    def setCustomer(self, new_costumer):
        """
        Sets the customer id to a new value
        """
        self.__customer_id = new_costumer

    def setRentedDate(self, new_rented):
        """
        Sets the rented date to a new value
        """
        self.__rented_date = new_rented

    def setReturnDate(self, new_returned):
        """
        Sets the return date to a new value
        """
        self.__return_date = new_returned

    def setCost (self, new_cost):
        """
        Sets the cost to a new value
        """
        self.__cost = new_cost

    def setInsurance(self, new_insurance):
        """
        Sets the insurance to a new value
        """
        self.__insurance = new_insurance
    
    def getOrderId(self):
        """
        Returns the order id
        """
        return self.__order_id

    def getCarPlate(self):
        """
        Returns the car plate
        """
        return self.__car_plate

    def getCustomerId(self):
        """
        Returns the customer id
        """
        return self.__customer_id

    def getRentedDate(self):
        """
        Returns the rented date
        """
        return self.__rented_date

    def getReturnDate(self):
        """
        Returns the return date
        """
        return self.__return_date

    def getCost (self):
        """
        Returns the cost
        """
        return self.__cost

    def getInsurance(self):
        """
        Returns the insurance
        """
        return self.__insurance
    
    def __repr__(self):
        """
        Prints out all the variables with commas between
        """
        return "{},{},{},{},{},{},{}".format(self.getOrderId(), self.getCarPlate(), 
                                             self.getCustomerId(), self.getRentedDate(), 
                                             self.getReturnDate(), self.getCost(), 
                                             self.getInsurance())

    def __str__(self):
        """
        Prints out a menu of all the variables
        """
        return "{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}\n{:<15}{}".format(
                                             "Pöntunarnúmer:", self.getOrderId(),
                                             "Viðskiptavinur:", self.getCustomerId(),
                                             "Númer Bíls:", self.getCarPlate(),
                                             "Fyrsti dagur:", self.getRentedDate(),
                                             "Skiladagur:", self.getReturnDate(),
                                             "Kostnaður:", self.getCost(),
                                             "Tryggingar:", self.getInsurance())