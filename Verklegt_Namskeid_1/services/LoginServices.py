from models.Employee import Employee
from repositories.EmployeeRepository import EmployeeRepository
class LoginServices():
    def __init__(self):
        self.__employee_repository = EmployeeRepository()
        self.__employees = self.__employee_repository.getEmployees()

    def isValidLogin(self, employee_id, password):
        """
        This method checks if the user ID is valid and if the password matches the ID
        """
        if str(employee_id) in self.__employees:
            return self.__employees[employee_id].getPassword() == password
        return False