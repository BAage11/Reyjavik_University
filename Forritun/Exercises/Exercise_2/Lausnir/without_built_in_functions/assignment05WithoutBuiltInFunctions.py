size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

lowest_value = my_list[0]

for index in range(1, len(my_list)) :
    if my_list[index] < lowest_value :
        lowest_value = my_list[index]

print("The lowest value in the list is {} ".format(lowest_value))