
from Sports import SportRegistration
from Members import MemberRegistration
from Member_in_Sport import MemberInSportRegistration


class MainMenu():
    reg_sport = SportRegistration()
    reg_member = MemberRegistration()
    reg_member_in_sport = MemberInSportRegistration()
    
    
    print("\na) Register a new sport\nb) Register a new member\nc) Sign member up for a particular sport\nPress 'q' to quit.")
    choices = ['a', 'b', 'c']
    user_input = input("\nChoice: ")

    while user_input != 'q' or user_input != 'Q':
        try:
            if user_input == 'a':
                print("\nTEAM REGISTRATION")
                sport_name = input("Sport name: ")
                sport_reg = reg_sport.registerSport(sport_name)
                if sport_reg:
                    print("\nSport has been registered.")
        
            elif user_input == 'b':
                print("\nMEMBER REGISTRATION")
                member_name = str(input("Name: "))
                member_phone = int(input("Phone number: "))
                member_email = str(input("Email: "))
                member_yob = int(input("Year of birth: "))
                reg_member.registerMember(member_name, member_phone, member_email, member_yob)
        
            elif user_input == 'c':
                curr_sport = reg_sport.head
                curr_member = reg_member.head

                print("\nMEMBER SPORT SIGN UP")
                member = input("Member name: ")
                sport = input("Sport name: ")
                        
                while curr_sport != None or curr_sport != sport:
                    curr_sport = curr_sport.next
                if curr_sport == None:
                    print("Sport is not registered yet.")

                while curr_member != None or curr_member != member:
                    curr_member = curr_member.next
                if curr_member == None:
                    print("Member is not registered yet.")

                if curr_member and curr_member:
                    reg_member_in_sport.member_sport(sport, member)

            elif user_input == 'q' or user_input == 'Q':
                quit()
        except:
            print("Invalid input.")
    
        print("\na) Register a new sport\nb) Register a new member\nc) Sign member up for a particular sport\nPress 'q' to quit.")
        user_input = input("\nChoice: ")        


#    sport = SportRegistration()
#    sport.registerSport("Soccer")
#    sport.registerSport("Curling")
#    sport.registerSport("Basketball")
#    print(sport)
#    print("Number of registered sports: ", len(sport), "\n")
#
#    member = MemberRegistration()
#    member.registerMember("Benjamin Aage", 6942051, "benjamin18@ru.is", 1983)
#    member.registerMember("Aníta Bj0rg", 6922460, None, 2007)
#    member.registerMember("Marianne Ósk", 6921595, "marianneoskbn@gmail.com", 1948)
#    member.registerMember("Birgir Þ.", 8965765, "birgirth@hotmail.com", 1938)
#    member.registerMember("Rikard Arnar", 6959283, "rikard@gmail.com", 1988)
#    print(member)
#    print("Number of registered members: ", len(member), "\n")