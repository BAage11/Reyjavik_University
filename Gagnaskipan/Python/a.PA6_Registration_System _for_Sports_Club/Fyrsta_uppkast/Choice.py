from Sports import SportRegistration
from Members import MemberRegistration
from Member_in_Sport import MemberInSportRegistration

class UserChoice():
    def __init__(self):
        self.reg_sport = SportRegistration()
        self.reg_member = MemberRegistration()
        self.reg_member_in_sport = MemberInSportRegistration()

    def validChoice(self, user_choice):
        if user_choice == 'a':          # Register new sport
            print("\nTEAM REGISTRATION")
            sport_name = input("Sport name: ")

            sport_reg = self.reg_sport.registerSport(sport_name)
            if sport_reg:
                print("\nSport has been registered.")
                return None
            else:
                return sport_reg

    
        elif user_choice == 'b':            # Register new member
            print("\nMEMBER REGISTRATION")
            member_name = str(input("Name: "))
            member_phone = int(input("Phone number: "))
            member_email = str(input("Email: "))
            member_yob = int(input("Year of birth: "))

            member_reg = self.reg_member.add_member(member_name, member_phone, member_email, member_yob)
            if member_reg:
                print("\nMember has been registered.")
                return None
            else:
                return member_reg


        elif user_choice == 'c':            # Register member in sport
            curr_sport = self.reg_sport.head
            
            print("\nMEMBER SPORT SIGN UP")
            member = input("Member name: ")
            sport = input("Sport name: ")

            while curr_sport != None or curr_sport != sport:
                curr_sport = curr_sport.next
            if curr_sport == None:
                print("Sport is not registered yet.")

            find_member = self.reg_member.get_by_name(member)
            if find_member == False:
                print("Member is not registered yet.")

            if curr_sport and find_member:
                self.reg_member_in_sport.member_sport(sport, find_member.member_name)
                return None


        elif user_choice == 'q' or user_choice == 'Q':
            return 1
