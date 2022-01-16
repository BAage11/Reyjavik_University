import csv
from models.Employee import Employee

class EmployeeRepository():
    def __init__(self): 
        """
        Creates an empty dictonary for the employees
        """
        self.__employees = {}
    
    def getEmployees(self):
        """
        Fetches the data from the Employees.csv file
        """
        with open("./database/Employees.csv", "r", encoding="utf-8-sig") as employee_database:
            csv_reader = csv.DictReader(employee_database)
            for line in csv_reader:
                number = line["number"]
                ssn = line["ssn"]
                name = line["name"]
                password = line["password"]
                self.__employees[number] = Employee(name, ssn, number, password)
        return self.__employees

    def addEmployee(self, employee):
        """
        Adds a employee to the employees.csv file
        """
        self.getEmployees()
        self.__employees[employee.getId()] = employee
        with open("./database/Employees.csv", "a+", encoding="utf-8") as employee_database:
            employee_database.write(employee.__repr__() + "\n")
        return None
    
    def deleteEmployee(self, employee_id):
        """
        Deletes a employee from the system
        """
        if str(employee_id) in self.__employees:
            self.__employees.pop(str(employee_id))     
            with open("./database/Employees.csv", "w", encoding="utf-8") as employee_database:
                employee_database.write("number,ssn,name,password\n")
                for employee in self.__employees:
                    employee_database.write(self.__employees[employee].__repr__() + "\n")
        return None