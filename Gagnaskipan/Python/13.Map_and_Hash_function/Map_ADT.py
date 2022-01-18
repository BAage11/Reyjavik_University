# ADT - Tag sem inniheldur aðgerð sem er notað, án þess að vita hvernig það er útfært. Í þessu verkefni er útfært hins vegar ADT gagnatakið.

class Node():
    def __init__(self, key = 0, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next

class Map():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, value):
        new_node = Node(key, value, self.head)
        self.head = new_node
        self.size += 1

    def find(self, key):
        try:
            next_item = self.head
            while next_item.key != key:
                next_item = next_item.next
            else:
                return next_item.data
        except:
            return None

    def update(self, key, value):
        item = self.head
        while item.key != key:
            item = item.next
        item.data = value

    def remove(self, key):
        find_item = self.head
        while find_item.next.key != key:
            find_item = find_item.next
        if find_item.next.key == key:
            find_item.next.data = None
            find_item.next.key = None
        find_item.next = find_item.next.next
            
    def __len__(self):
        return self.size

    def __str__(self):
        next_item = self.head
        ret_str = ""
        while next_item != None:
            ret_str += str(next_item.key) + " " + str(next_item.data) + "\n"
            next_item = next_item.next            
        return ret_str



the_map = Map()

print("\nPUT IN KEY AND VALUE TO THE MAP:")
the_map.insert(15, "dog")
the_map.insert(1, "cat")
the_map.insert(33, "horse")
the_map.insert(4, "elephant")
print(the_map)

print("FIND VALUES FROM A GIVEN KEY:")
print("Key number 33 has value:", the_map.find(33))
print("Key number 99 has value:", the_map.find(99))

print("\nCHANGE A VALUE FROM A GIVEN KEY:")
the_map.update(15, "snail")
print(the_map)

print("REMOVING KEY AND DATA FROM THE MAP, FROM A GIVEN KEY:")
the_map.remove(33)
print(the_map)

print("SIZE OF THE MAP IS:", len(the_map))
