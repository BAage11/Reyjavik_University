import os
from services.EmployeeAddServices import EmployeeAddServices
from services.CustomerAddServices import CustomerAddServices
class EmployeeAddUi():
    def __init__(self):
        self.__employeeService = EmployeeAddServices()
        self.__userService = CustomerAddServices()
        self.__number = ""
        self.__name = ""
        self.__ssn = ""
        self.__password = ""

    def addUserMenu(self):
        """
        Prints out the menu to add an employee
        """
        os.system('cls')
        print("--- Skrá Nýjan Starfsmann ---")
        self.__number = self.__employeeService.generateId()
        self.__name = self.getName()
        self.__ssn = self.getSsn()
        print ("Lykilorð verður að vera lengra en 6 stafir og innihalda a.m.k. tvo tölustafi og einn hástaf.")
        self.__password = self.getPassword()
        print("-------------------------------")
        self.__employeeService.addEmployee(self.__name, self.__ssn,
                                       self.__number, self.__password)
        print("Starfsmaður", self.__name, "hefur verið bætt við")
        print(self.__name, "hefur innskráningarnúmerið", self.__number)
        input("")

    def getName(self):
        """
        The user inputs a name 
        """
        name = input("{:<15}".format("Nafn:"))
        while self.__userService.isValidName(name) == False:
            print("Þetta er ekki löglegt nafn!")
            name = input("{:<15}".format("Nafn:"))
        return name

    def getSsn(self):
        """
        The user inputs a social security number
        """
        ssn = input("{:<15}".format("Kennitala:"))
        while self.__userService.isValidSsn(ssn) == False:
            print("Þetta er ekki lögleg kennitala!")
            ssn = input("{:<15}".format("Kennitala:"))
        return ssn

    def getPassword(self):
        """
        The user inputs a password
        """
        password = input("{:<15}".format("Lykilorð:"))
        while self.__employeeService.isValidPassword(password) == False:
            print("Þetta er ekki löglegt lykilorð!")
            password = input("{:<15}".format("Lykilorð:"))
        return password

