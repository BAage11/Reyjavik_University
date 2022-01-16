class Vehicle:

    def __init__(self, the_license, the_year):
        self.license = the_license
        self.year = the_year
        self.fee = 0.0
        self.weight = 0.0

    def __str__(self):
        return "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(self.license,
                                             self.year, self.weight, self.fee)

    def get_license(self):
        return self.license

    def get_year(self):
        return self.year

    def get_weight(self):
        return self.weight

    def get_fee(self):
        return self.fee

    def set_fee(self, the_fee):
        self.fee = the_fee

    def set_weight(self, the_weight):
        self.weight = the_weight


C_WEIGHT1 = 3000
C_WEIGHT2 = 5000
C_FEE1 = 30
C_FEE2 = 40
C_FEE3 = 50

class Car(Vehicle):
    def __init__(self, the_license, the_year, the_style): 
        Vehicle.__init__(self, the_license, the_year)
        self.style = the_style

    def __str__(self):
        return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.get_license(), self.get_year(), self.style, self.get_weight(), self.get_fee())
    
    def set_weight(self, the_weight):
        Vehicle.set_weight(self, the_weight)
        if the_weight < C_WEIGHT1:
            self.set_fee(C_FEE1)
        elif the_weight < C_WEIGHT2:
            self.set_fee(C_FEE2)
        else:
            self.set_fee(C_FEE3)


T_WEIGHT1 = 3000
T_WEIGHT2 = 5000
T_WEIGHT3 = 10000

T_FEE1 = 40
T_FEE2 = 50
T_FEE3 = 60
T_FEE4 = 70

class Truck(Vehicle):
    
    def __init__(self, the_license, the_year, the_wheels):
        Vehicle.__init__(self, the_license, the_year) 
        self.wheels = the_wheels


    def set_weight(self, the_weight):
        Vehicle.set_weight(self, the_weight)

        if the_weight < T_WEIGHT1:
            self.set_fee(T_FEE1)
        elif the_weight < T_WEIGHT2:
            self.set_fee(T_FEE2)
        elif the_weight < T_WEIGHT3: 
            self.set_fee(T_FEE3)
        else:
            self.set_fee(T_FEE4)

    def __str__(self):
        return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.get_license(),
                 self.get_year(), self.wheels, self.get_weight(), self.get_fee())


M_CC1 = 50
M_CC2 = 200
M_FEE1 = 10
M_FEE2 = 20
M_FEE3 = 35

class Motorbike(Vehicle):
    def __init__(self, the_license, the_year):
        Vehicle.__init__(self, the_license, the_year)
        self.cc = 0

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.get_license(), self.get_year(), self.cc, self.get_fee())

    def get_CC(self):
        return self.cc

    def set_CC(self, the_cc):
        self.cc = the_cc
        if self.cc < M_CC1:
            self.set_fee(M_FEE1)
        elif self.cc < M_CC2: 
            self.set_fee(M_FEE2)
        else:
            self.set_fee(M_FEE3)

    


def main():
    
    # Create some vehicles
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)

    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)

    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight() ))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee() ))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
    print()

    #Put the four vehicles into a list. 
    # Then loop through the list and call the print function for each of the vehicles.
    # You have to implement this part of the main program!

    vehicles = [v1, c1, t1, b1]
    for vehicle in vehicles:
        print(vehicle)

    v1 = c1
    print(v1)
    print()

main()
