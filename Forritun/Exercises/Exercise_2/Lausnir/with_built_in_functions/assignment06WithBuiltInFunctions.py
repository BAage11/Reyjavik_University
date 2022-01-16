size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

total_sum = sum(my_list)

print("The sum of all the values in the list is {} ".format(total_sum))