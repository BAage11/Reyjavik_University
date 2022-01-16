class InsuranceServices():
    """ 
    Class to check if the given input of the user is valid or not
    """
    def __init__(self):
        self.__valid_choices = ["j", "n"]

    def isValidChoice(self, choice):
        """
        Checks if the choice is valid
        """
        return choice in self.__valid_choices

    