from sortedcontainers import SortedDict

class Member():
    def __init__(self, name, phone, email, year):
        self.member_name = name
        self.member_phone = phone
        self.member_email = email
        self.member_birth_year = year

    def __str__(self):
        """ Return a string with registered information about members in system. """
        return "Member: {}\nPhone: {}\nEmail: {}\nBirth Year: {}\n".format(self.member_name, self.member_phone, self.member_email, self.member_birth_year)


class MemberRegistration():
    def __init__(self):
        self.member_map = SortedDict()
        self.name_map = SortedDict()
        self.phone_map = SortedDict()
        self.email_map = SortedDict()
        self.year_map = SortedDict()
        self.unique_id = 1

    def add_member(self, name, phone, email, year):
        """ Register new member. """
        for _, value in self.member_map.items():
            if value == name:
                return False
        else:        
            self.member_map[self.unique_id] = Member(name, phone, email, year)
            self.name_map[name] = self.unique_id
            self.phone_map[phone] = self.unique_id
            self.email_map[email] = self.unique_id
            self.year_map[year] = self.unique_id
            self.unique_id += 1
            return True


    def get_by_name(self, name):
        """ Returns the data for the current member, by name given (if exist). """
        try:
            name_id = self.name_map[name]
            return self.member_map[name_id]
        except:
            return False

    def get_by_phone(self, phone):
        """ Returns the data for current member, by phone number given (if exist). """
        try:
            phone_id = self.phone_map[phone]
            return self.member_map[phone_id]
        except:
            return False

    def get_by_email(self, email):
        """ Returns the data for current member, by email given. """
        try:
            email_id = self.email_map[email]
            return self.member_map[email_id]
        except:
            return False

    def get_by_year_of_birth(self, year):
        """ Returns the data for current member, by given year of birth. """
        try:
            year_id = self.year_map[year]
            return self.member_map[year_id]
        except:
            return False

    def get_by_id(self, unique_id):
        """ Returns the data for current member, by given ID. """
        try:
            return self.member_map[unique_id]
        except:
            return False
    
    def remove_member(self, name):
        """ Removing a registered member, by given name. """
        for key, value in self.member_map.items():
            if value.member_name == name:
                del self.name_map[name]
                del self.phone_map[value.member_phone]
                del self.email_map[value.member_email]
                del self.year_map[value.member_birth_year]
                del self.member_map[key]
                return True
        return False
        
    def get_all_members_by_name(self):
        """ Returns a list of all registered members. """
        members = []
        for name in self.name_map:
            members.append(name)
        return members

    def get_all_members_by_age(self):
        """ Returns a list of members, sorted by year of birth 
            (oldest first / youngest last). """
        members = []
        for __,value in self.year_map.items():
            members.append(self.get_by_id(value))
        return members
