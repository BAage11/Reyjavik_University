from Double_Linked_List import DoubleLinkedList, Empty


class DLL_Set():
    def __init__(self):
        super.__init__()
    
    def add_item(self, data):
        super.add_to_set(data)

    def delete_item(self, data):          ##################
        super.delete_set_item(data)

    def find_value(self, data):
        super.find(data)

    def get_all_items(self):
        super.print_forward()
        super.print_backward()

    def union(self, set_a, set_b):
        pass

    def intersection(self, set_a, set_b):
        pass

    def difference(self, set_a, set_b):
        pass

    def subset(self, set_a, set_b):
        pass

    def equals(self, set_a, set_b):
        pass


print("\nPrófanir\n\n")
dll_set = DLL_Set()

print("\nAdd item:")
dll_set.add_item(67)
dll_set.add_item(343)
dll_set.add_item(90)
dll_set.add_item(894)
dll_set.add_item(67)
print(dll_set.get_all_items())

print("\nDelete item:")
dll_set.delete_item(90)
print(dll_set.get_all_items())

print("\nFind value:")
dll_set.find_value(343)
dll_set.find_value(5555)

print("\nUnion of two sets:")
set_a = set("blabla", 666, 1, 932, 10, 14)
set_b = set(932, "ekkert", 881, 443, 1)
print(dll_set.union(set_a, set_b))

print("\nIntersection of two sets:")
set_a = set("blabla", 666, 1, 932, 10, 14)
set_b = set(932, "ekkert", 881, 443, 1)
print(dll_set.intersection(set_a, set_b))

print("\nDifference of two sets:")
set_a = set("blabla", 666, 1, 932, 10, 14)
set_b = set(932, "ekkert", 881, 443, 1)
print(dll_set.difference(set_a, set_b))

print("\nSubset of two sets:")
set_a = set("blabla", 666, 1, 932, 10, 14)
set_b = set(932, "ekkert", 881, 443, 1)
print(dll_set.subset(set_a, set_b))

print("\nEquals of two sets:")
set_a = set("blabla", 666, 1, 932, 10, 14)
set_b = set(932, "ekkert", 881, 443, 1)
print(dll_set.equals(set_a, set_b))
