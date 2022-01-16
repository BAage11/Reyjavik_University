class CarMainMenuServices():
    """
    Class to check if the given choice of the user
    is a valid option from the given menu
    """
    def __init__(self):
        self.__valid_choices = ["1","2","3","4"]
    
    def isValidChoice(self, choice):
        """
        Checks if the choice is valid
        """
        return choice in self.__valid_choices