
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
        """ User shall be able to register new sport - Name of sport. """ 
        curr_node = self.head
        if curr_node == None:
            self.head = self.tail = Sport(sport_name, None)
        else:
            while curr_node != None:
                if curr_node.sport_name == sport_name:
                    return "Sport has already been registered."
                curr_node = curr_node.next
            self.tail.next = Sport(sport_name, None)
            self.tail = self.tail.next
        self.sport_count += 1
        return True


    def __len__(self):
        """ Returns the number of registered sports. """
        return self.sport_count


    def __str__(self):
        """ Returns the name of sports that have been registered / are currently registered. """
        curr_node = self.head
        ret_str = ""
        while curr_node != None:
            ret_str += curr_node.sport_name + "\n"
            curr_node = curr_node.next
        return ret_str
