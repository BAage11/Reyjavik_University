def create_list(size) :
    numbers = []
    while size > 0 :
        value = int(input("Enter a value: "))
        numbers.append(value)
        size -= 1
    return numbers


def get_average_of_list(the_list) :
    total_sum = 0

    for value in the_list :
        total_sum += value
    
    average = float(total_sum) / len(the_list)
    return average


def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    average = get_average_of_list(my_list)
    print("The average of all the values in the list is {} ".format(average))

main()