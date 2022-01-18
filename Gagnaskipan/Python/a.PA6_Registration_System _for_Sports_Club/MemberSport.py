

class Node():
    def __init__(self, sport = None, member = None, next = None):
        self.sport = sport
        self.member = member
        self.next = next

    def __str__(self):
        """ Return a string with registered sport and member. """
        return "Sport: {}  Member: {}\n".format(self.sport, self.member)


class MemberSportRegistration():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_member_to_sport(self, member_name, sport_name):
        """ Add a member to a registered sport. """
        curr_node = self.head

        if self.head == None:
            self.head = self.tail = Node(sport_name, member_name)
            return True
        
        while curr_node != None:
            if curr_node.sport == sport_name:
                if curr_node.member == member_name:
                    return False
                else:
                    self.tail.next = Node(sport_name, member_name)
                    self.tail = self.tail.next
                    return True
        
            self.tail.next = Node(sport_name, member_name)
            self.tail = self.tail.next
            return True
        
        self.tail.next = Node(sport_name, member_name)
        self.tail = self.tail.next
        return True
        

    def unregister(self, member, sport):
        """ Removes registration for a member in a specific sport. """
        curr_node = self.head
        
        if self.head.member == member:
            if self.head.sport == sport:
                self.head.next = self.head
                return True
        
        while curr_node.next != None:
            if curr_node.next.member == member:
                if curr_node.next.sport == sport:
                    curr_node.next = curr_node.next.next
                    return True
        
            curr_node.next = curr_node.next.next
        
        return False


    def get_all_members_by_sport(self, sport):
        """ Returns a list of members within a specific sport. """
        members = []
        curr_node = self.head
        
        while curr_node != None:
            if curr_node.sport == sport:
                members.append(curr_node.member)
            curr_node = curr_node.next
        
        return members


    def get_member_registered_sports(self, name):
        """ Returns a list of sport(s) which a member is registered in. """
        sports = []
        curr_node = self.head
        
        while curr_node != None:
            if curr_node.member == name:
                sports.append(curr_node.sport)
            curr_node = curr_node.next
        
        return sports


    def sport_removed(self, sport):
        """ Removes a registered sport from the system. """
        curr_node = self.head
        
        if self.head != None:
            if self.head.sport == sport:
                self.head = self.head.next
        
        if self.head == None:
            return None

        while curr_node.next != None:
            if curr_node.next.sport == sport:
                curr_node.next = curr_node.next.next
                break
            curr_node.next = curr_node.next.next


    def member_removed(self, member):
        """ When a member is removed from system, all sports that the member has been registered for is also removed from system here. """
        curr_node = self.head
        
        if self.head == None:
            return None

        elif self.head != None:
            if self.head.member == member:
                self.head = self.head.next
        
        while curr_node.next != None:
            if curr_node.next.member == member:
                curr_node.next = curr_node.next.next
            curr_node.next = curr_node.next.next
