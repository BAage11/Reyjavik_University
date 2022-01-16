size = int(input("Please enter the size of the list: "))

my_list = []

while size > 0 :
    value = int(input("Enter a value: "))
    my_list.append(value)
    size -= 1

target = int(input("Enter a value to count: "))
counter = my_list.count(target)

print("{} occurs {} times in the list. ".format(target, counter))