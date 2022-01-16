import datetime
from repositories.CarRepository import CarRepository
from repositories.OrderRepository import OrderRepository
class CarSearchServices():
    def __init__(self):
        self.__car_repo = CarRepository()
        self.__order_repo = OrderRepository()
        self.__cars = self.__car_repo.getCars()
        self.__orders = self.__order_repo.getOrders()
        self.__valid_choices = ["1", "2", "3", "4"]
        self.__30_day_months = ["4", "6", "9", "11"]

    def isValidChoice(self, choice):
        """
        Checks if the choice is valid
        """
        return choice in self.__valid_choices
    
    def isValidCar(self, choice, cars_count):
        """
        Checks if the car is valid
        """
        try:
            return int(choice) <= cars_count and int(choice) > 0
        except:
            return False
    
    def isValidYear(self, year, form_date = 0):
        """
        Checks if the year is valid
        """
        curr_year = datetime.date.today().year
        if form_date == 0:
            return year.isdigit() and int(year) >= curr_year
        return year.isdigit() and int(year) >= int(form_date[:4])
    
    def isValidMonth(self, month, year, from_date = 0):
        """
        Checks if the month is valid
        """
        try:
            curr_year = datetime.date.today().year
            curr_month = datetime.date.today().month
            if int(year) > curr_year:
                curr_month = 0
            if from_date == 0:
                return int(month) > 0 and int(month) < 13 and int(month) >= curr_month
            else:
                date = from_date.split("-")
                from_date_month = int(date[1])
                return int(month) > 0 and int(month) < 13 and int(month) >= from_date_month
        except:
            return False
    
    def isValidDay(self, day, month, year, form_date = 0):
        """
        Checks if the day is valid
        """
        try:
            curr_year = datetime.date.today().year
            curr_day = datetime.date.today().day
            if int(year) > curr_year:
                curr_day = 0
            if form_date == 0:
                if int(month) == 2:
                    return int(day) > 0 and int(day) < 29 and int(day) >= curr_day
                elif month in self.__30_day_months:
                    return int(day) > 0 and int(day) < 31 and int(day) >= curr_day
                else:
                    return int(day) > 0 and int(day) < 32 and int(day) >= curr_day
            else:
                date = form_date.split("-")
                from_date_month = int(date[1])
                from_date_day = int(date[2])
                if int(month) > from_date_month:
                    from_date_day = 0
                if int(month) == 2:
                    return int(day) > 0 and int(day) < 29 and int(day) > from_date_day
                elif month in self.__30_day_months:
                    return int(day) > 0 and int(day) < 31 and int(day) > from_date_day
                else:
                    return int(day) > 0 and int(day) < 32 and int(day) > from_date_day
        except:
            return False
    

    def getCarsOrder(self, plate):
        """
        Gets all orders for specific car
        """
        orders = []
        for order in self.__orders:
            if self.__orders[order].getCarPlate() == plate:
                orders.append(self.__orders[order])
        return orders

    def isCarAvailable(self, car, from_date, return_date):
        """
        Checks if the car is available
        """
        orders = self.getCarsOrder(car.getPlateNumber())
        from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
        return_date = datetime.datetime.strptime(return_date, "%Y-%m-%d").date()
        for order in orders:
            order_return = datetime.datetime.strptime(
                                    order.getReturnDate(), 
                                    "%Y-%m-%d").date()
            order_rented = datetime.datetime.strptime(
                                    order.getRentedDate(), 
                                    "%Y-%m-%d").date()
            if(from_date < order_rented < return_date):
                return False
            if(from_date < order_return < return_date):
                return False
        return True
        
    def carNotInOrders(self, plate):
        """
        Gets cars that don't have an order
        """
        for order in self.__orders:
            if self.__orders[order].getCarPlate() == plate:
                return False
        return True

    def getValidCars(self, from_date, return_date, car_type):
        """
        Gets all valid cars
        """
        valid_cars = []
        for car in self.__cars:
            if self.__cars[car].getCarType() == car_type:
                if self.carNotInOrders(car):
                    valid_cars.append(self.__cars[car])
                elif self.isCarAvailable(self.__cars[car], from_date, return_date):
                    valid_cars.append(self.__cars[car])
        return valid_cars

  