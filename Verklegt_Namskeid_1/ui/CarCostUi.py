from ui.CarSearchUi import CarSearchUi
from services.CarCostServices import CarCostServices

class CarCostUi():
    def __init__(self):
        self.__car_services = CarCostServices()

    def menu(self):
        """
        Prints out how much it costs to rent a car for a specific amount of time
        """
        days = self.getDays()
        car_type = CarSearchUi().getCarType()
        price = self.__car_services.getPriceWithoutInsurance(days, car_type)
        print("Að leigja {} í {} daga kostar {} krónur".format(car_type, days, price))
        print("Ýttu á enter til að halda áfram")
        input("")

    def getDays(self):
        """
        Gets the user to input how many days the car will be rented for
        """
        print("Hversu marga daga er verið að leigja?")
        days = input("> ")
        while self.__car_services.isValidDays(days) == False:
            print("Þetta er ekki löglegur fjöldi daga")
            days = input("> ")
        return days


