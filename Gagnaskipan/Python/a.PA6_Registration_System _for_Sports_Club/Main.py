from Members import MemberRegistration
from Sports import SportRegistration
from MemberSport import MemberSportRegistration

member_registration = MemberRegistration()
sport_registration = SportRegistration()
member_sport_registration = MemberSportRegistration()


choice = True
while choice != False:
    print("\n----- REGISTRATION SYSTEM -----")
    print()
    
    print("1.  New sport registration\n2.  New member registration\n3.  Sign member for a particular sport\n\n4.  Remove member from sport\n5.  Remove member from system\n6.  Remove sport from system\n\n7.  List all members\n8.  Select specific member\n9.  Get detailed information about a member\n\n10. List all sports\n11. Get information about a sport")
    
    choice = input("\nChoice: ")
    
    if choice == str(1):
        print("\n----- NEW SPORT REGISTRATION ----\n")
        
        sport = input("Sport name: ")
        new_sport = sport_registration.registerSport(sport)
        
        if new_sport:
            print("'" + str(sport) + "' has been registered.\n")
            print("-"*35)
        else:
            print("'" + str(sport) + "' is already registered.\n")
            print("-"*35)


    elif choice == str(2):
        print("\n----- NEW MEMBER REGISTRATION-----\n")

        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        year = input("Year: ")

        new_member = member_registration.add_member(name, phone, email, year)

        if new_member:
            print("\n'" + str(name) + "' has been registered.\n")
            print("-"*35)
        else:
            print("'" + str(name) + "' is already registered.\n")
            print("-"*35)
        

    elif choice == str(3):
        print("\n-----MEMBER REGISTRATION FOR SPORT-----\n")
        
        name = input("Member name: ")
        sport = input("Sport name: ")

        check_member = member_registration.get_by_name(name)
        check_sport = sport_registration.get_sport(sport)

        if check_member and check_sport:
            new_member_in_sport = member_sport_registration.add_member_to_sport(name, sport)
            
            if new_member_in_sport:
                print("'" + str(name) + "' has been registered in '" + str(sport) + "'.\n")
                print("-"*35)
            else:
                print("Member is already registed in sport '" + str(sport) + "'.\n")
                print("-"*35)
        
        elif check_member and not check_sport:
            print("'" + str(sport) + "' is not a registered sport.\n")
            print("-"*35)
        
        elif not check_member and check_sport:
            print("'" + str(name) + "' is not a registered member.\n")
            print("-"*35)
        
        elif not check_member and not check_sport:
            print("Member '" + str(name) + "' and the sport '" + str(sport) + "' are both not yet registered.\n")
            print("-"*35)
 

    elif choice == str(4):
        print("\n----- UNREGISTER MEMBER FROM SPORT -----\n")
        
        name = input("Member name: ")
        sport = input("Sport name: ")

        check_member = member_registration.get_by_name(name)
        check_sport = sport_registration.get_sport(sport)

        if check_member and check_sport:
            unregister_member_in_sport = member_sport_registration.unregister(name, sport)
            
            if unregister_member_in_sport:
                print("'" + str(name) + "' has been removed from '" + str(sport) + "'.\n")
                print("-"*35)
            else:
                print("'" + str(name) + "' could not be found registered for '" + str(sport) + "'.\n")
                print("-"*35)
        
        elif check_member and not check_sport:
            print("'" + str(sport) + "' is not a registered sport.\n")
            print("-"*35)
        
        elif not check_member and check_sport:
            print("'" + str(name) + "' is not a registered member.\n")
            print("-"*35)
        
        elif not check_member and not check_sport:
            print("Member '" + str(name) + "' and the sport '" + str(sport) + "' are both not yet registered.\n")
            print("-"*35)
         

    elif choice == str(5):
        print("\n----- REMOVE MEMBER FROM SYSTEM -----\n")
        
        name = input("Name of member: ")
        
        member_sport_registration.member_removed(name)
        remove_member = member_registration.remove_member(name)
        
        if remove_member:
            print("'" + str(name) + "' has been removed from system.\n")
            print("-"*35)
        else:
            print("Member '" + str(name) + "' could not be found in system.\n")       
            print("-"*35)


    elif choice == str(6):
        print("\n----- REMOVE SPORT FROM SYSTEM ----\n")
        
        sport = input("Sport name: ")
        
        member_sport_registration.sport_removed(sport)
        remove_sport = sport_registration.remove_sport(sport)
        
        if remove_sport:
            print("'" + str(sport) + "' has been removed from system.\n")
            print("-"*35)
        else:
            print("Sport '" + sport + "' could not be found in system.\n")
            print("-"*35)

    
    elif choice == str(7):
        print("\n----- LIST OF MEMBERS -----\n")
        print("Order by:\na) Name\nb) Age\nc) Sport\n")
        
        order_by = input("Choice: ")

        if order_by == 'a':
            members_by_name = member_registration.get_all_members_by_name()
            
            if members_by_name == []:
                print("No members are currently registered.\n")
            else:
                print("\nMembers by name:")
                for i in members_by_name:
                    print(str(i))
            print("-"*35)
        
        elif order_by == 'b':
            members_by_age = member_registration.get_all_members_by_age()
        
            if members_by_age == []:
                print("No members are currently registered.\n")
            else:
                print("\nMembers by age:")
                for j in members_by_age:
                    print(str(j))
            print("-"*35)
        
        elif order_by == 'c':
            sport = input("Members of which sport? ")
            members_by_sport = member_sport_registration.get_all_members_by_sport(sport)
        
            if members_by_sport == []:
                print("No members are currently registered in '" + str(sport) + "' and/or sport is not registered.\n")
            else:
                print("\nMembers in the sport '" + str(sport) + "':")
                for k in members_by_sport:
                    print(str(k))
            print("-"*35)
        
        else:
            print("Not a possible option.\n")
            print("-"*35)


    elif choice == str(8):
        print("\n----- GET INFORMATION ABOUT A MEMBER -----\n")
        print("By:\na) Name\nb) Phone\nc) Email\nd) Age\n")
        
        get_by = input("Choice: ")

        if get_by == 'a':
            name = input("What is the member name? ")
            member_by_name = member_registration.get_by_name(name)
        
            if member_by_name:
                print("\nInformation about chosen member from given name:")
                print("\n" + str(member_by_name) + "\n")
                print("-"*35)
            else:
                print("\nMember '" + str(name) + "' was not recognized (could not be found).\n")
                print("-"*35)
        
        elif get_by == 'b':
            phone = input("What is the member phone number? ")
            member_by_phone = member_registration.get_by_phone(phone)
        
            if member_by_phone:
                print("\nInformation about member from given phone number:")
                print("\n" + str(member_by_phone) + "\n")
                print("-"*35)
            else:
                print("\nThe phone number '" + str(phone) + "' was not recognized (could not be found).\n")
                print("-"*35)
        
        elif get_by == 'c':
            email = input("What is the member email? ")
            member_by_email = member_registration.get_by_email(email)
        
            if member_by_email:
                print("\nInformation about member from given email:")
                print("\n" + str(member_by_email) + "\n")
                print("-"*35)
            else:
                print("\nThe email '" + str(email) + "' was not recognized (could not be found).\n")
                print("-"*35)
        
        elif get_by == 'd':
            birth_year = input("What year was the member born? ")
            member_by_year = member_registration.get_by_year_of_birth(birth_year)
        
            if member_by_year:
                print("\nInformation about member for given birth year:")
                print("\n" + str(member_by_year) + "\n")
                print("-"*35)
            else:
                print("\nNo member could be found that is born in the year '" + str(birth_year) + "'.")
                print("-"*35)
        
        else:
            print("Not a possible option.\n")
            print("-"*35)



    elif choice == str(9):
        print("\n----- GET DETAILED INFORMATION ABOUT A MEMBER -----\n")
        
        members_by_name = member_registration.get_all_members_by_name()
        
        print("Registered members:")
        if members_by_name:
            for i in members_by_name:
                print(str(i))
        
            member = input("\nSelect a member: ")
            for j in members_by_name:
                if j == member:
                    print("\nMember information:")
                    print(member_registration.get_by_name(member))
                    sports = member_sport_registration.get_member_registered_sports(member)
                    print("Member is registered in the following sport(s):")
        
                    if sports == []:
                        print("None")
                    else:
                        for k in sports:
                            print(str(k))
                    print()
                    print("-"*35)        
        else:
            print("There are currently no registered members.\n")
            print("-"*35)

   
    elif choice == str(10):
        print("\n----- LIST OF ALL REGISTERED SPORTS -----")
        
        sports = sport_registration.get_all_sports()
        
        if sports:
            print("\nSports currently registered:")
            for i in sports:
                print(i)
            print()
            print("-"*35)
        else:
            print("\nNo sports are currently registered.\n")
            print("-"*35)


    elif choice == str(11):
        print("\n----- INFORMATION ABOUT SPORT ------\n")
        
        sport = input("What sport would you like to see? ")
        
        members_in_sport = member_sport_registration.get_all_members_by_sport(sport)
        check_sport = sport_registration.get_sport(sport)
        
        if check_sport:
            if members_in_sport:
                print("\nMembers in the sport '" + str(sport) + "':")
                for i in members_in_sport:
                    print(i)
                print("-"*35)
            else:
                print("No members are currently registered for the sport '" + str(sport) + "'.\n")
                print("-"*35)
        else:
            print("Sport '" + str(sport) + "' is not registered.\n")


    else:
        print("\n----- LOGGING OUT -----\n")
        for_real = input("Are you sure you want to log out (y/n)? ")
        if for_real == 'y' or for_real == 'Y':       
            choice = False
        else:
            choice = True