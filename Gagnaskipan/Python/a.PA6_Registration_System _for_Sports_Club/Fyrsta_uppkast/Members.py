
class Member():
    def __init__(self, name = None, phone = None, email = None, year = None, next = None):
        self.member = name
        self.phone_number = phone
        self.email = email
        self.birth_year = year
        self.next = next


class MemberRegistration():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def registerMember(self, name, phone, email, year_of_birth):
        """ User shall be able to register new member - Name, Phone, Email, Year of birth. """
        curr_node = self.head
        if curr_node == None:
            self.head = self.tail = Member(name, phone, email, year_of_birth, None)
        else:
            while curr_node != None:
                if curr_node.member == name:
                    return "Member already registered."
                curr_node = curr_node.next
            self.tail.next = Member(name, phone, email, year_of_birth, None)
            self.tail = self.tail.next
        self.size += 1
        return True


    def remove_member(self, name):
        if self.head.member == name:
            self.header = self.header.next
        else:
            curr_node = self.head
            while curr_node.next != None:
                pass




    def __len__(self):
        """ Returns the number of registered members. """
        return self.size


    def __str__(self):
        """ Returns the name of sports that have been registered / are currently registered. """
        curr_node = self.head
        count = 1
        ret_str = ""
        while curr_node != None:
            ret_str += "Member number " + str(count) + ": " + curr_node.member + "\n"
            curr_node = curr_node.next
            count += 1
        return ret_str
