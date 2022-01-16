from repositories.CustomerRepository import CustomerRepository

class CustomerChangeServices():
    def __init__(self):
        self.__customer_repository = CustomerRepository()
        self.__valid_choices = ["1", "2", "3", "4", "5", "6"]
        self.__customer = ""

    def getCustomer(self, ssn):
        """
        Returns specific customer
        """
        customers = self.__customer_repository.getCustomers()
        self.__customer = customers[ssn]
        return customers[ssn]

    def isValidChoice(self, choice):
        """
        Checks if the choice is valid
        """
        return choice in self.__valid_choices

    def changeSsn(self, new_ssn):
        """
        Changes the ssn of a customer
        """
        self.__customer_repository.deleteCustomer(self.__customer.getSsn())
        self.__customer.setSsn(new_ssn)
        self.__customer_repository.addCustomer(self.__customer)

    def changeName(self, new_name):
        """
        Changes the name of a customer
        """
        self.__customer_repository.deleteCustomer(self.__customer.getSsn())
        self.__customer.setName(new_name)
        self.__customer_repository.addCustomer(self.__customer)

    def changeAddress(self, new_address):
        """
        Changes the address of a customer
        """
        self.__customer_repository.deleteCustomer(self.__customer.getSsn())
        self.__customer.setAddress(new_address)
        self.__customer_repository.addCustomer(self.__customer)

    def changePhone(self, new_phone):
        """
        Changes the phone of a customer
        """
        self.__customer_repository.deleteCustomer(self.__customer.getSsn())
        self.__customer.setPhone(new_phone)
        self.__customer_repository.addCustomer(self.__customer)

    def changeCountry(self, new_country):
        """
        Changes the country of a customer
        """
        self.__customer_repository.deleteCustomer(self.__customer.getSsn())
        self.__customer.setCountry(new_country)
        self.__customer_repository.addCustomer(self.__customer)
