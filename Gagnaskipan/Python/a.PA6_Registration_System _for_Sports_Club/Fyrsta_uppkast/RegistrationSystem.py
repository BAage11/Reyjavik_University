
class MainMenu():
    def __init__(self):
        self.choices = ['a', 'b', 'c', 'q']


    def userChoice(self):
        print("\n----- Registration system for sports club -----")
        choice = self.getChoice()
        while choice == False:
            print("Not a valid input.")
            choice = self.getChoice()
        if choice:
            return choice
        

    def getChoice(self):
        print("\na) Register a new sport\nb) Register a new member\nc) Sign member up for a particular sport\nPress 'q' to quit.")

        user_input = input("\nChoice: ")
        for valid_choice in self.choices:
            if user_input == valid_choice:
                return user_input
        return False

