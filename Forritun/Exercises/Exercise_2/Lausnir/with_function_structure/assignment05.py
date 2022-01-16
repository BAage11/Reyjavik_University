def create_list(size) :
    numbers = []
    while size > 0 :
        value = int(input("Enter a value: "))
        numbers.append(value)
        size -= 1
    return numbers


def get_lowest_value_in_list(the_list) :
    lowest_value = the_list[0]

    for index in range(1, len(the_list)) :
        if the_list[index] < lowest_value :
            lowest_value = the_list[index]
    
    return lowest_value


def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    lowest_value = get_lowest_value_in_list(my_list)

    print("The lowest value in the list is {} ".format(lowest_value))

main()