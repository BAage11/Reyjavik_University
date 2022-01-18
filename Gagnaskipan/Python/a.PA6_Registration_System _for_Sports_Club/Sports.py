
class Sport():
    def __init__(self, sport_name = None, next = None):
        self.sport_name = sport_name
        self.next = next


class SportRegistration():
    def __init__(self):
        self.head = None
        self.tail = None
        self.sport_count = 0


    def registerSport(self, sport_name):
        """ Register a new sport within the system. """
        curr_node = self.head
        if self.head == None:
            self.head = self.tail = Sport(sport_name)
            self.sport_count += 1
            return True
        while curr_node != None:
            if curr_node.sport_name == sport_name:
                return False
            curr_node = curr_node.next
        self.tail.next = Sport(sport_name)
        self.tail = self.tail.next
        self.sport_count += 1
        return True


    def get_sport(self, sport):
        """ Check if a sport is registered in the system. """
        curr_node = self.head
        if self.head == None:
            return False
        while curr_node != None:
            if curr_node.sport_name == sport:
                return True
            curr_node = curr_node.next
        return False

    def get_all_sports(self):
        """ Returns a list of all sports registered within the system. """
        curr_node = self.head
        sports = []
        while curr_node != None:
            sports.append(curr_node.sport_name)
            curr_node = curr_node.next
        return sports


    def remove_sport(self, sport):
        """ Removing a sport that is registered in the system. """
        curr_node = self.head
        if self.head == None:
            return None
        elif self.head.sport_name == sport:
            self.head = self.head.next
            return True
        while curr_node != None:
            if curr_node.next.sport_name == sport:
                curr_node.next = curr_node.next.next
                return True
            curr_node = curr_node.next
        return False


    def __len__(self):
        """ Return the number of sports registered within the system. """
        return self.sport_count


    def __str__(self):
        """ Returning a string of all sports registered within the system. """
        curr_node = self.head
        ret_str = ""
        while curr_node != None:
            ret_str += curr_node.sport_name + "\n"
            curr_node = curr_node.next
        return ret_str
