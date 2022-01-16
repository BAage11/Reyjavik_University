# Write a program that:
# Reads in two lists of integers from the user and converts them to sets and prints out the # sets.
# Allows the user to repeatedly perform intersection, union and difference on the two sets # and prints out the result of each operation

input1 = input("Input a list of integers separated with a comma: ").split(",")
input2 = input("Input a list of integers separated with a comma: ").split(",")

set_int1 = set()
for i in input1:
  set_int1.add(int(i))

set_int2 = set()
for j in input2:
  set_int2.add(int(j))

print(set_int1)
print(set_int2)

choice = ""
while choice != str(4):
  print("1. Intersection")
  print("2. Union")
  print("3. Difference")
  print("4. Quit")
  
  choice = input("Set operation: ")
  if choice == str(1):
    intersect = set_int1.intersection(set_int2)
    print(intersect)
  if choice == str(2):
    union = set_int1.union(set_int2)
    print(union)
  if choice == str(3):
    diff = set_int1.difference(set_int2)
    print(diff)
  