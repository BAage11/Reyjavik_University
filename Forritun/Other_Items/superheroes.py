class Superteam:
    def __init__(self, name="", age=0, superpower="n"):
        self.name = name
        self.age = age
        self.superpower = superpower
    
    def setName(self, name=""):
        self.name = name
        return self.name
    
    def setAge(self, age=0):
        self.age = age
        return self.age
    
    def setSuperPower(self, superpower=""):
        self.superpower = superpower
        if self.superpower == "f":
            self.superpower = "Flying"
        elif self. superpower == "g":
            self.superpower = "Giant"
        elif self.superpower == 'h':
            self.superpower = "Hacker"
        elif self.superpower == "n":
            self.superpower = "None"
        else:
            self.superpower = "Weakling"
        return self.superpower
    
    def __str__(self):
        return "{} ({}): {}".format(self.name, self.age, self.superpower)


# Main program starts here:
def create_some_heroes():
    hero = Superteam()
    hero.SetName("Ásgeir")
    hero.SetAge(20)
    hero.SetSuperPower("h")
    print(hero)

create_some_heroes()


