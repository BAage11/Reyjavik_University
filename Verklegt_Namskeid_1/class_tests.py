#================================================================================================================
#                                                   tests on models classes
#================================================================================================================
from models.Person import Person
from models.Employee import Employee
from models.Customer import Customer
from models.Car import Car
from models.Order import Order
from models.CreditCard import CreditCard

# tests on Person Class
person1 = Person("Jón","2411992159")
assert str(person1) == str("SSN:           2411992159"
                         "\nName:          Jón")
person1.setSsn("1234567890")
assert str(person1) == str("SSN:           1234567890"
                         "\nName:          Jón")
person1.setName("Kalli")
assert str(person1) == str("SSN:           1234567890"
                         "\nName:          Kalli")
assert person1.__repr__() == str("1234567890,Kalli")

# tests on Employee class
employee1 = Employee("Jón","2411992159","10","kalli123")
assert employee1.__repr__() == "10,2411992159,Jón,kalli123"
employee1.setId("12")
assert employee1.__repr__() == "12,2411992159,Jón,kalli123"
employee1.setPassword("nyttpw")
assert employee1.__repr__() == "12,2411992159,Jón,nyttpw"
assert employee1.login("12","nyttpw") == True
assert employee1.login("10","kalli123") == False
assert str(employee1) == str("Employee id:   12"
                           "\nSSN:           2411992159"
                           "\nName:          Jón")    

# tests on Customer class
customer1 = Customer("Gunna","2587469831","Flúðasel 170","5891578","Ísland")
assert customer1.__repr__() == "2587469831,Gunna,Flúðasel 170,5891578,Ísland"
customer1.setAddress("Flúðasel 18")
assert customer1.__repr__() == "2587469831,Gunna,Flúðasel 18,5891578,Ísland"
customer1.setCountry("Kanada")
assert customer1.__repr__() == "2587469831,Gunna,Flúðasel 18,5891578,Kanada"
customer1.setName("Fjóla")
assert customer1.__repr__() == "2587469831,Fjóla,Flúðasel 18,5891578,Kanada"
customer1.setPhone("5812345")
assert customer1.__repr__() == "2587469831,Fjóla,Flúðasel 18,5812345,Kanada"
customer1.setSsn("2411992159")
assert customer1.__repr__() == "2411992159,Fjóla,Flúðasel 18,5812345,Kanada"
assert str(customer1) == str("SSN:           2411992159"
                           "\nName:          Fjóla"
                           "\nAddress:       Flúðasel 18"
                           "\nPhone:         5812345"
                           "\nCountry:       Kanada") 

# tests on Car class
car1 = Car("MO R58","Laus","Fólksbíll","5","95-okt","2015","15.000-25.000","Toyota","Blár")
assert car1.__repr__() == "MO R58,Laus,Fólksbíll,5,95-okt,2015,15.000-25.000,Toyota,Blár"
car1.setPlateNumber("NE W12")
assert car1.__repr__() == "NE W12,Laus,Fólksbíll,5,95-okt,2015,15.000-25.000,Toyota,Blár"
car1.setStatus("Útleigu")
assert car1.__repr__() == "NE W12,Útleigu,Fólksbíll,5,95-okt,2015,15.000-25.000,Toyota,Blár"
car1.setCarType("Jeppi")
assert car1.__repr__() == "NE W12,Útleigu,Jeppi,5,95-okt,2015,15.000-25.000,Toyota,Blár"
car1.setSeats("2")
assert car1.__repr__() == "NE W12,Útleigu,Jeppi,2,95-okt,2015,15.000-25.000,Toyota,Blár"
car1.setFuelType("Dísel")
assert car1.__repr__() == "NE W12,Útleigu,Jeppi,2,Dísel,2015,15.000-25.000,Toyota,Blár"
car1.setModel("2017")
assert car1.__repr__() == "NE W12,Útleigu,Jeppi,2,Dísel,2017,15.000-25.000,Toyota,Blár"
car1.setPriceRange("15.000-20.000")
assert car1.__repr__() == "NE W12,Útleigu,Jeppi,2,Dísel,2017,15.000-20.000,Toyota,Blár"
car1.setManufacturer("Nissan")
assert car1.__repr__() == "NE W12,Útleigu,Jeppi,2,Dísel,2017,15.000-20.000,Nissan,Blár"
car1.setColor("Rauður")
assert car1.__repr__() == "NE W12,Útleigu,Jeppi,2,Dísel,2017,15.000-20.000,Nissan,Rauður"
assert str(car1) == str("Númeraplata:   NE W12"
                      "\nStatus bíls:   Útleigu"
                      "\nTýpa:          Jeppi"
                      "\nFjöldi sæta:   2"
                      "\nEldsneyti:     Dísel"
                      "\nÁrgerð:        2017"
                      "\nFramleiðandi:  Nissan"
                      "\nLitur:         Rauður"
                      "\nVerðflokkur:   15.000-20.000")

# tests on Order class
order1 = Order("1","MO R58","2587469831","2017-01-02","2017-01-12","25.000","10.000","43")
assert order1.__repr__() == "1,MO R58,2587469831,2017-01-02,2017-01-12,25.000,10.000,43"
order1.setCarPlate("KY S73")
assert order1.__repr__() == "1,KY S73,2587469831,2017-01-02,2017-01-12,25.000,10.000,43"
order1.setCost("100.000")
assert order1.__repr__() == "1,KY S73,2587469831,2017-01-02,2017-01-12,100.000,10.000,43"
order1.setCustomer("2411992159")
assert order1.__repr__() == "1,KY S73,2411992159,2017-01-02,2017-01-12,100.000,10.000,43"
order1.setEmployee("1")
assert order1.__repr__() == "1,KY S73,2411992159,2017-01-02,2017-01-12,100.000,10.000,1"
order1.setRentedDate("2017-01-03")
order1.setReturnDate("2017-01-13")
assert order1.__repr__() == "1,KY S73,2411992159,2017-01-03,2017-01-13,100.000,10.000,1"
order1.setInsurance("15.000")
assert order1.__repr__() == "1,KY S73,2411992159,2017-01-03,2017-01-13,100.000,15.000,1"
assert str(order1) == str("Pöntunarnúmer: 1"
                        "\nViðskiptavinur:2411992159"
                        "\nNúmer Bíls:    KY S73"
                        "\nFyrsti dagur:  2017-01-03"
                        "\nSkiladagur:    2017-01-13"
                        "\nKostnaður:     100.000"
                        "\nTryggingar:    15.000"
                        "\nStarfsmaður:   1")

# tests on CreditCard class
card1 = CreditCard("2587469831","1111222233334444","2018-12","999")
assert card1.__repr__() == "2587469831,1111222233334444,2018-12,999"
card1.setCustomerSsn("2411992159")
assert card1.__repr__() == "2411992159,1111222233334444,2018-12,999"
card1.setCreditCardNumber("2111222233334444")
assert card1.__repr__() == "2411992159,2111222233334444,2018-12,999"
card1.setExpirationDate("2018-10")
assert card1.__repr__() == "2411992159,2111222233334444,2018-10,999"
card1.setCvc("666")
assert card1.__repr__() == "2411992159,2111222233334444,2018-10,666"
assert str(card1) == str("Kennitala:     2411992159"
                       "\nKortanúmer:    2111222233334444")

#================================================================================================================
#                                                   tests on ui classes
#================================================================================================================
from ui.AddUserUi import AddUserUi
from ui.MainMenuUi import MainMenuUi
from ui.CustomerUi import CustomerUi
from ui.CarRegisterUi import CarRegisterUi
from ui.CarMainMenuUi import CarMainMenuUi
from ui.LoginUi import LoginUi
from ui.InsuranceUi import InsuranceUi
from ui.CustomerInformationUi import UserInformationUi
from ui.SearchCustomerUi import SearchCustomerUi
from ui.SpecificCustomerUi import SpecificCustomerUi
from ui.CarSearchUi import CarSearchUi
from ui.RentCarUi import RentCarUi
from ui.AllCustomersUi import AllCustomersUi
from ui.CarRemoveUi import CarRemoveUi
from ui.CarShowAllUi import CarShowAllUi
# tests on AddUserUi class
userui = AddUserUi()
userui.addUserMenu()
# tests on MainMenuUi class
main_menu_ui = MainMenuUi()
main_menu_ui.mainMenu()
# tests on CustomerUi
customer_ui = CustomerUi()
customer_ui.customerMenu()
# tests on CarRegisterUi
car_register = CarRegisterUi()
car_register.addCarMenu()
# tests on CarMainMenyUi
car_main_menu = CarMainMenuUi()
car_main_menu.carMainMenu()
# tests on LoginUi
login_menu = LoginUi()
login_menu.loginMenu()
# tests on InsuranceUi()
insurance_tests = InsuranceUi()
print(insurance_tests.AddInsuranceMenu())
# tests on customerInformationUi
cust_info_test = UserInformationUi()
cust_info_test.userInfoMenu()
# tests on SearchCustomerUi()
search_cust_tests = SearchCustomerUi()
search_cust_tests.searchUserMenu()
# tests on SpecificCustomerUi
spcific_cust = SpecificCustomerUi("2587469831")
spcific_cust.printInformation()
#tests on CarSearchServices()
car_search = CarSearchUi()
car_search.searchCarMenu()
# tests on RentCarUi()
rent_car = RentCarUi()
rent_car.isNewCustomer()
# tests on AllCustomersUi
all_cust = AllCustomersUi()
all_cust.printInformation()
# tests on CarRemoveUi()
car_remove = CarRemoveUi()
car_remove.carRemoveMenu()
# tests on CarShowAllUi()
show_all_cars = CarShowAllUi()
show_all_cars.printInformation()
#================================================================================================================
#                                                tests on repository classes
#================================================================================================================
from repositories.CustomerRepository import CustomerRepository
from repositories.EmployeeRepository import EmployeeRepository
from repositories.CarRepository import CarRepository
# # tests on CustomerRepository class
# customer_test = CustomerRepository()
# customers = customer_test.getCustomers()
# customer_test.addCustomer(customer1)
# customer_test.deleteCustomer("2411992159")
# # tests on EmployeeRepository class 
# employee_test = EmployeeRepository()
# employees = employee_test.getEmployees()
# employee_test.addEmployee(employee1)
# employee_test.deleteEmployee("2")
# # tests on CarRepository class
# car_test = CarRepository()
# cars = car_test.getCars()
# car_test.addCar(car1)
# car_test.deleteCar("EW R69")




