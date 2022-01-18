
class Node():
    def __init__(self, sport = None, member = None):
        self.sport = sport
        self.member = member


class MemberInSportRegistration():
    def __init__(self):
        self.head = None
        self.tail = None

    def member_sport(self, sport_name, member_name):
        curr_node = self.head
        while curr_node != None:
            if curr_node.sport == sport_name:
                if curr_node.member == member_name:
                    print(member_name, " is already registered in ", sport_name)
                else:
                    self.tail.next = Node(sport_name, member_name)
                    self.tail = self.tail.next
                    return
        self.tail.next = Node(sport_name, member_name)
        self.tail = self.tail.next
        