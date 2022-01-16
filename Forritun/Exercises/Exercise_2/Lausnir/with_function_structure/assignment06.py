def create_list(size) :
    numbers = []
    while size > 0 :
        value = int(input("Enter a value: "))
        numbers.append(value)
        size -= 1
    return numbers


def get_sum_of_list(the_list) :
    total_sum = 0

    for value in the_list :
        total_sum += value
    return total_sum


def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    total_sum = get_sum_of_list(my_list)
    print("The sum of all the values in the list is {} ".format(total_sum))

main()


