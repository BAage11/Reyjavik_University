import os
from services.InsuranceServices import InsuranceServices
class InsuranceUi():
    def __init__(self):
        self.__insurance_services = InsuranceServices()
        self.__insurance_cost = 0

    def AddInsuranceMenu(self):
        """
        Prints out the menu and adds the insurance cost together
        """
        os.system('cls')
        print("--------- Tryggingar ---------")
        self.__insurance_cost += self.getInsuranceOne()
        self.__insurance_cost += self.getInsuranceTwo()
        self.__insurance_cost += self.getInsuranceThree()        
        print("------------------------------")
        return self.__insurance_cost

    def getInsuranceOne(self):
        """
        Prints out info about the first type of insurance
        """
        print("\nTrygging 1:"
              "\nKaskótrygging bíls"
              "\nBætir tjón á bíl sem ökumaður veldur."
              "\nTryggingataki velur upphæð eigináhættu sem hann ber í hverju tjóni."
              "\nVerð 30.000kr")
        if self.getChoiceInput():
            return 30000
        return 0
        
    def getInsuranceTwo(self):
        """
        Prints out info about the second type of insurance
        """
        print("\nTrygging 2:"
              "\nBílrúðutrygging"
              "\nTrygging fyrir framrúðu, hliðarrúðu og afturrúðu."
              "\nVerð 5.000kr")
        if self.getChoiceInput():
            return 5000
        return 0
    
    def getInsuranceThree(self):
        """
        Prints out info about the third type of insurance
        """
        print("\nTrygging 3:"
              "\nÁbyrgðartrygging bíls - Eigináhætta"
              "\nUpphæð sem tryggingataki ber í hverju tjóni."
              "\nVerð 50.000kr")
        if self.getChoiceInput():
            return 50000
        return 0

    def getChoiceInput(self):
        """
        The user inputs whether he wants to add insurance or not
        """
        choice = input("{:<15}".format('Bæta við tryggingu?(j/n)')).lower()
        while self.__insurance_services.isValidChoice(choice) == False:
            print(choice, "Er hvorki j eða n!")
            choice = input("{:<15}".format("Bæta við tryggingu?(j/n)"))
        return choice == "j"