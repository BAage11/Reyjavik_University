size = int(input("Please enter the size of the list: "))

my_list = []

for i in range(size):
    value = int(input("value no.{} ".format(i + 1)))
    my_list.append(value)

my_list_without_duplicates = []

for value in my_list :
    if value not in my_list_without_duplicates :
        my_list_without_duplicates.append(value)

print("The list:", my_list)
print("The list without duplicates:", my_list_without_duplicates)

