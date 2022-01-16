def create_list(size) :
    numbers = []
    while size > 0 :
        value = int(input("Enter a value: "))
        numbers.append(value)
        size -= 1
    return numbers


def get_highest_value_in_list(the_list) :
    highest_value = the_list[0]

    for index in range(1, len(the_list)) :
        if the_list[index] > highest_value :
            highest_value = the_list[index]
    
    return highest_value


def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    highest_value = get_highest_value_in_list(my_list)

    print("The highest value in the list is {} ".format(highest_value))

main()