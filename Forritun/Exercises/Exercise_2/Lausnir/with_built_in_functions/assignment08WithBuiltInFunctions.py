size = int(input("Please enter the size of the list: "))

my_list = []

for i in range(size):
    value = int(input("value no.{} ".format(i + 1)))
    my_list.append(value)

my_list_without_duplicates = list(set(my_list))

print("The list:", my_list)
print("The list without duplicates:", my_list_without_duplicates)