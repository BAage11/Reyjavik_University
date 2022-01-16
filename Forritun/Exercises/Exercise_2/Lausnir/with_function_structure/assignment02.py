def create_list(size) :
    numbers = []
    while size > 0 :
        value = int(input("Enter a value: "))
        numbers.append(value)
        size -= 1
    return numbers


def value_in_list(the_list, target) :
    for index, _ in enumerate(the_list) :
        if the_list[index] == target :
            return True
    return False


def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    target = int(input("Enter a value to search for in the list: "))
    if value_in_list(my_list, target) :
        print("{} is in the list". format(target))
    else :
        print("{} is not in the list". format(target))

main()