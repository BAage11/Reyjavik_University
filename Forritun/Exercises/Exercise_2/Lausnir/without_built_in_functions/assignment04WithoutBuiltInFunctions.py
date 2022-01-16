size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

highest_value = my_list[0]

for index in range(1, len(my_list)) :
    if my_list[index] > highest_value :
        highest_value = my_list[index]

print("The highest value in the list is {} ".format(highest_value))