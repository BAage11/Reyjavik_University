from ui.CarMainMenuUi import CarMainMenuUi
from ui.CustomerUi import CustomerUi
from ui.EmployeeAddUi import EmployeeAddUi
from ui.CarRegisterUi import CarRegisterUi
from ui.CarRentUi import CarRentUi
from ui.CarCostUi import CarCostUi
from services.MainMenuServices import MainMenuServices
class MainMenuUi():
    def __init__(self):
        self.__main_menu_services = MainMenuServices()
        self.__car_ui = CarMainMenuUi()
        self.__cust_ui = CustomerUi()
        self.__empl_ui = EmployeeAddUi()
        self.__rent_ui = CarRentUi()
        self.__cost_ui = CarCostUi()

    def mainMenu(self):
        """
        Prints out the Menu you can choose from in MainMenu
        """
        print("---------- Heimasvæði ----------")
        print("1. Leigja bíl")
        print("2. Bílar")
        print("3. Skrá nýjan starfsmann")
        print("4. Viðskiptavinir")
        print("5. Birta Verðlista")
        print("6. Reikna kostnað án trygginga")
        print("7. Útskrá")
        print("--------------------------------")
        return self.executeChoice(self.getChoice())

    def printPrices(self):
        """
        Prints out the prices
        """
        print("------ Verðlisti -------")
        print("\n----- Verð á bílum -----")
        print("Smábíll: kr.10.000")
        print("Fólksbíll: kr.10.000")
        print("Jepplingur: kr.15.000")
        print("Jeppi: kr.20.000")
        print("\n-- Verð á tryggingum --")
        print("Kaskótrygging: kr.30.000")
        print("Bílrúðutrygging: kr.5.000")
        print("Ábyrgðartrygging: kr.50.000")
        print("Ýttu á enter til að halda áfram")
        input("")

    def getChoice(self):
        """
        Gets the choice from the user
        """
        print("Veldu aðgerð")
        choice = input("> ")
        while self.__main_menu_services.isValidChoice(choice) == False:
            print(choice,"Er ekki lögleg aðgerð, reyndu aftur")
            choice = input("> ")
        return choice

    def executeChoice(self, choice):
        """
        Executes the choice the user chose
        """
        if(choice == "1"):
            self.__rent_ui.isNewCustomer()
        elif choice == "2":
            self.__car_ui.carMainMenu()
        elif choice == "3":
            self.__empl_ui.addUserMenu()
        elif choice == "4":
            self.__cust_ui.customerMenu()
        elif choice == "5":
            self.printPrices()
        elif choice == "6":
            self.__cost_ui.menu()
        elif choice == "7":
            print("Útskrái starfsmann...")
            print("Útskráning lokið.")
            return False