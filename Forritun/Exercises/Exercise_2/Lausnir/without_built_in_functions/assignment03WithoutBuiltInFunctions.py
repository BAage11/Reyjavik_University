size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

target = int(input("Enter a value to count: "))
counter = 0

for index, value in enumerate(my_list) :
    if value == target:
        counter += 1

print("{} occurs {} times in the list. ".format(target, counter))