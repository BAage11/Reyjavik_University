def create_list(size) :
    numbers = []
    
    for i in range(size):
        value = int(input("value no.{} ".format(i + 1)))
        numbers.append(value)
    
    return numbers

def eliminate_duplicates_from_list(the_list) :
    list_without_duplicates = []

    for value in the_list :
        if value not in list_without_duplicates :
            list_without_duplicates.append(value)

    return list_without_duplicates


def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    my_list_without_duplicates = eliminate_duplicates_from_list(my_list)

    print("The list:", my_list)
    print("The list without duplicates:", my_list_without_duplicates)

main()




