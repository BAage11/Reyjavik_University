size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

lowest_value = min(my_list)

print("The lowest value in the list is {} ".format(lowest_value))