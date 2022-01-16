import os
from services.CarMainMenuServices import CarMainMenuServices
from ui.CarRegisterUi import CarRegisterUi
from ui.CarShowAllUi import CarShowAllUi
from ui.CarSearchUi import CarSearchUi
from ui.CarAlreadyRentedUi import CarAlreadyRentedUi
class CarMainMenuUi:
    def __init__(self):
        self.__car_main_menu_services = CarMainMenuServices()
        self.__car_register_ui = CarRegisterUi()
        self.__show_cars_ui = CarShowAllUi()
        self.__search_cars_ui = CarSearchUi()
        self.__car_already_rented_ui = CarAlreadyRentedUi()

    def carMainMenu(self):
        """
        Prints out the main menu for the user to choose between
        """
        os.system('cls')
        print("---------- Allir Bílar ---------")
        print("1. Sjá alla lausa bíla")
        print("2. Sjá alla bíla í útleigu")
        print("3. Skrá nýjan bíl")
        print("4. Fara á Heimasvæði")
        print("--------------------------------")
        self.executeChoice(self.getChoice())

    def getChoice(self):
        """
        Gets what the user inputs as his choice
        """
        print("Veldu aðgerð")
        choice = input("> ")
        while not self.__car_main_menu_services.isValidChoice(choice):
            print(choice,"Er ekki lögleg aðgerð")
            choice = input("> ")
        return choice

    def executeChoice(self, choice):
        """
        Executes the users choice
        """ 
        if choice == "1":
            self.__show_cars_ui.printInformation()
        elif choice == "2":
            self.__car_already_rented_ui.printInformation()
        elif choice == "3":
            self.__car_register_ui.addCarMenu()
        


    