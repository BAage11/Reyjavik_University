class CarRentServices():
    def __init__(self):
        self.__valid_choices = ["1", "2", "3"]

    def isValidChoice(self, choice):
        """
        checks if the users choice is valid
        """
        return choice in self.__valid_choices