def create_list(size) :
    numbers = []
    while size > 0 :
        value = int(input("Enter a value: "))
        numbers.append(value)
        size -= 1
    return numbers


def count_occurrences_of(the_list, target) :
    counter = 0

    for value in the_list :
        if target == value:
            counter += 1
    return counter


def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    target = int(input("Enter a value to count: "))
    count = count_occurrences_of(my_list, target)

    print("{} occurs {} times in the list. ".format(target, count))

main()