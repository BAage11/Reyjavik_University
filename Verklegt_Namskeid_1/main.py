import os
from ui.LoginUi import LoginUi
from ui.MainMenuUi import MainMenuUi
from services.CarRentCheckServices import CarRentCheckServices
def main():
    login_ui = LoginUi()
    employee_id = login_ui.loginMenu()
    main_menu = MainMenuUi()
    car_check = CarRentCheckServices()
    choice = None
    while choice == None:
        car_check.carRentCheck()
        car_check.carReturnCheck()
        os.system('cls')
        choice = main_menu.mainMenu()
main()