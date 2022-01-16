from models.Person import Person
class CreditCard(Person):
    """
    Class to create information about a customers creditcard information,
    for payment insurance 
    """
    def __init__(self, customer_ssn, credit_card_number, exp_date, cvc, choice = "Ógreitt"):
        self.__customer_ssn = customer_ssn
        self.__credit_card_number = credit_card_number
        self.__exp_date = exp_date
        self.__cvc = cvc
        self.__choice = choice
    
    def setCustomerSsn(self, new_ssn):
        """
        Sets the customer ssn to a new value
        """
        self.__customer_ssn = new_ssn
    
    def setCreditCardNumber(self, new_credit_card_number):
        """
        Sets the credit card number to a new value
        """
        self.__credit_card_number = new_credit_card_number
    
    def setExpirationDate(self, new_exp_date):
        """
        Sets the expiration date to a new value
        """
        self.__exp_date = new_exp_date
    
    def setCvc(self, new_cvc):
        """
        Sets the cvc to a new value
        """
        self.__cvc = new_cvc
    
    def setChoice(self, new_choice):
        """
        Sets the choice to a new value
        """
        self.__choice = new_choice

    def getCustomerSsn(self):
        """
        Returns the customer ssn
        """
        return self.__customer_ssn
    
    def getCreditCardNumber(self):
        """
        Returns the credit card number
        """
        return self.__credit_card_number
    
    def getExpirationDate(self):
        """
        Returns the expiration date
        """
        return self.__exp_date
    
    def getCvc(self):
        """
        Returns the cvc
        """
        return self.__cvc
    
    def getChoice(self):
        """
        Returns the choice
        """
        return self.__choice
    
    def __repr__(self):
        """
        Prints out all the variables with commas between
        """
        return "{},{},{},{},{}".format(self.getCustomerSsn(), self.getCreditCardNumber(),
                                    self.getExpirationDate(), self.getCvc(),
                                    self.getChoice())

    def __str__(self):
        """
        Prints out a menu of all the variables
        """
        return "{:<15}{}\n{:<15}{}\n{:<15}{}".format("Kennitala:", self.getCustomerSsn(),
                                           "Kortanúmer:", self.getCreditCardNumber(),
                                           "Status:", self.getChoice())