from RegistrationSystem import MainMenu
from Choice import UserChoice

def main():
    main_menu = MainMenu()
    user_choice = main_menu.userChoice()
    choice = UserChoice()
    choice.validChoice(user_choice)
   
    choice = None
    while choice == None:
        choice = UserChoice()
        choice.validChoice(user_choice)


main()