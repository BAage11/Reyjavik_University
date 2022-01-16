size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

target = int(input("Enter a value to search for in the list: "))
value_in_list = False
for index, value in enumerate(my_list) :
    if my_list[index] == target :
        value_in_list = True
        break

if value_in_list :
    print("{} is in the list". format(target))
else :
    print("{} is not in the list". format(target))
