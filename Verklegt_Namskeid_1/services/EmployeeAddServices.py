from models.Employee import Employee
from repositories.EmployeeRepository import EmployeeRepository
class EmployeeAddServices():
    def __init__(self):
        self.__employeeRepo = EmployeeRepository()

    def isValidPassword(self, password):
        """
        Checks if the password is valid
        """
        digits = [char.isdigit() for char in password]
        upper_chars = [char.isupper() for char in password]
        if len(password) > 6 and len(digits) > 1 and len(upper_chars) > 0:
            return True
        else:
            return False

    def generateId(self):
        """
        Generates an employee id
        """
        employees = self.__employeeRepo.getEmployees()
        if len(employees) != 0:
            max_id = max(employees, key=int)
            employee_id = int(max_id)+1
            return employee_id
        else:
            return 1

    def addEmployee(self, name, ssn, number, password):
        """
        Adds the employee
        """
        new_employee = Employee(name, ssn, number, password)
        self.__employeeRepo.addEmployee(new_employee)







