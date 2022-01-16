size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

highest_value = max(my_list)

print("The highest value in the list is {} ".format(highest_value))