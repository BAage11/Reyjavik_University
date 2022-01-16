def create_list(size) :
    numbers = []
    while size > 0 :
        value = int(input("Enter a value: "))
        numbers.append(value)
        size -= 1
    return numbers

def main() :
    size = int(input("Please enter the size of the list: "))
    my_list = create_list(size)
    
    print(my_list)

main()