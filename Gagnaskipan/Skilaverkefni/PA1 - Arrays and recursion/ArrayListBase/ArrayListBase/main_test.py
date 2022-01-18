import array_list
from array_list import *

# Bunch of tests - please make your own :)
# also, please make your own test output
# clearer than this is.  It helps!!

print("SOME STRING TESTS:")
arr_lis = ArrayList()
arr_lis.append("c")
arr_lis.append("e")
arr_lis.append("d")
arr_lis.print()
arr_lis.append("i")
arr_lis.append("h")
arr_lis.append("g")
arr_lis.print()
arr_lis.append("m")
arr_lis.append("o")
arr_lis.append("n")
arr_lis.print()
# print(arr_lis.size)
# print(arr_lis.capacity)
# print(arr_lis.arr)
try:
    print(arr_lis.get_first())
except Empty:
    print("The list is empty")
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_at(0))
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_at(7))
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_at(9))
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_last())
except Empty:
    print("The list is empty")
except IndexOutOfBounds:
    print("Index out of bounds")
arr_lis.print()
arr_lis.prepend("ra")
arr_lis.print()
arr_lis.insert("rb", 11)
arr_lis.print()
arr_lis.insert("rb", 10)
arr_lis.print()
arr_lis.insert("rc", 8)
arr_lis.print()
arr_lis.insert("rd", 0)
arr_lis.print()
arr_lis.set_at("iii", 5)
arr_lis.print()
arr_lis.set_at("rda", 13)
arr_lis.print()
arr_lis.remove_at(0)
arr_lis.print()
arr_lis.remove_at(7)
arr_lis.print()
arr_lis.remove_at(11)
arr_lis.print()
arr_lis.remove_at(10)
arr_lis.print()
arr_lis.sort()
arr_lis.print()
print("Clearing list")
arr_lis.clear()
print("list after clearing:")
arr_lis.print()
try:
    print(arr_lis.get_first())
except Empty:
    print("The list is empty")
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_last())
except Empty:
    print("The list is empty")
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_at(0))
except IndexOutOfBounds:
    print("Index out of bounds")


print("SOME INTEGER TESTS:")
arr_lis = ArrayList()
arr_lis.append(3)
arr_lis.append(5)
arr_lis.append(4)
arr_lis.print()
arr_lis.append(9)
arr_lis.append(8)
arr_lis.append(7)
arr_lis.print()
arr_lis.append(13)
arr_lis.append(15)
arr_lis.append(14)
arr_lis.print()
try:
    print(arr_lis.get_first())
except Empty:
    print("The list is empty")
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_at(0))
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_at(7))
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_at(9))
except IndexOutOfBounds:
    print("Index out of bounds")
try:
    print(arr_lis.get_last())
except Empty:
    print("The list is empty")
except IndexOutOfBounds:
    print("Index out of bounds")
arr_lis.print()
arr_lis.prepend(101)
arr_lis.print()
arr_lis.insert(102, 11)
arr_lis.print()
arr_lis.insert(102, 10)
arr_lis.print()
arr_lis.insert(103, 8)
arr_lis.print()
arr_lis.insert(104, 0)
arr_lis.print()
arr_lis.remove_at(0)
arr_lis.print()
arr_lis.remove_at(7)
arr_lis.print()
arr_lis.remove_at(11)
arr_lis.print()
arr_lis.remove_at(10)
arr_lis.print()
arr_lis.sort()
arr_lis.print()
arr_lis.remove_value(14)
arr_lis.print()
arr_lis.remove_value(102)
arr_lis.print()
arr_lis.insert_ordered(6)
arr_lis.print()
arr_lis.insert_ordered(1)
arr_lis.print()
arr_lis.insert_ordered(107)
arr_lis.print()