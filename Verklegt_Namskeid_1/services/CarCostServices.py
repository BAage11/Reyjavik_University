from ui.CarSearchUi import CarSearchUi
from repositories.CarRepository import CarRepository
from services.CarRentAgreementServices import CarRentAgreementServices
from ui.CarRegisterChangeUi import CarRegisterChangeUi

class CarCostServices():
    def __init__(self):
        self.__car_prices = {"Jeppi": "20.000", "Jepplingur": "15.000", "Fólksbíll": "12.000", "Smábíll": "10.000"}

    def getPriceWithoutInsurance(self, days, car_type):
        """
        Gets the price of the car without insurance
        """
        car_price_unstripped = self.__car_prices[car_type]
        car_price = int(car_price_unstripped.replace(".", ""))
        total_price = car_price * int(days)
        return total_price
    
    def isValidDays(self, days):
        """
        Checks if the number of days are valid
        """
        return days.isdigit() and int(days) > 0