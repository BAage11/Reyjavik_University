import getpass
from services.LoginServices import LoginServices


class LoginUi():
    def __init__(self):
        self.__log_in_service = LoginServices()

    def loginMenu(self):
        """
        Prints out the login menu
        """
        print("--------- Innskráning ---------")
        employee_id, password = self.getLogin()
        while self.__log_in_service.isValidLogin(employee_id, password) == False:
            print("Þetta er ekki löglegt nafn eða lykilorð")
            employee_id, password = self.getLogin()
        print("-------------------------------")
        return True

    def getLogin(self):
        """
        The user inputs an id and password to log in
        """
        employee_id = input("{:<15}".format("ID:"))
        password = getpass.getpass("{:<15}".format("Lykilorð:"))
        return employee_id, password