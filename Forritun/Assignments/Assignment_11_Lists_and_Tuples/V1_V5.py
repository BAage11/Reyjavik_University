# Question 1: List manipulation
# In this assignment, three functions are given (which you are NOT allowed to change) but you have to implement the main program.  The basic flow of the main program is to get a list from the user and allow the user to perform some manipulation on the list using two functions.  The list is printed out after both getting its elements from the user and after manipulating it.
# If the user decides to mutate ('m') the list, then two additional inputs are required from the user.
# If the user decides to remove ('r') an element from the list, the one additional input is required from the user.
# If the user neither mutates nor removes from the list, the list is printed out unchanged.


def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)


def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)


def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here


list_from_user = get_list()
print(list_from_user)

choice = input("Enter choice (m,r): ")

if choice == "m":
    pos, added = input("What index and what number? ").split(",")
    mutate_list(list_from_user, int(pos), int(added))

elif choice == "r":
    rem_val = input("Remove what index of list? ")
    remove_ch(list_from_user, int(rem_val))

print(list_from_user)

# -----------------------------------------------------------------------------------------------------------------
# Question 2: List to tuple
# Write a function that takes a list as a parameter, converts every element in the list to an integer and then returns a tuple comprising of these integer elements.
# If the function encounters a character such as 'p' that cannot be converted to an integer, it throws this error message on the screen: "Error. Please enter only integers." and returns an empty tuple.


def list_to_tuple(_list):
    a_tuple = []
    try:
        a_tuple = [int(i) for i in _list]
    except:
        print("Error. Please enter only integers.")

    return tuple(a_tuple)


a_list = input(
    "Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)

# -----------------------------------------------------------------------------------------------------------------
# Question 3: Sum of even numbers
# Write a function that takes a list L of integers as an argument and uses list comprehension to return the sum of the even integers in the list L.
# Hint: In your implementation, you can use some of the list functions discussed on page 349 in the textbook.


def get_list():
    a_list = input(
        "Enter elements of list separated by commas: ").strip().split(',')
    return a_list


def even_sum(a_list):
    b_list = [int(i) for i in a_list if int(i) % 2 == 0]
    return sum(b_list)


# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))

# -----------------------------------------------------------------------------------------------------------------
# Question 4: Email addresses
# Write a program that asks the user for email addresses, one at a time (until the user inputs 'q'), puts them into a list and then prints out a list of tuples of usernames and domains.


def get_emails():
    email_list = []
    email = input("Email address: ")
    while email != "q":
        email_list.append(email)
        email = input("Email address: ")
    return email_list


def get_names_and_domains(email_list):
    email_tuple = [tuple(i.split("@")) for i in email_list]
    return email_tuple


email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)

# -----------------------------------------------------------------------------------------------------------------
# Question 5: Transform
# Implement the transform function described in assignment 54 on page 417 in the textbook:
# It is often times advantageous to be able to transfer data between multiple lists while rearranging their order. For instance, say that list1 = [1,2,3,4,5,6,7,8,9] and you wish to add the numbers in the index range 4:7 of list1 to another list, list2, in reverse order while simultaneously removing them from list1. If list2 = [100,200], the result will be list2 = [100,200,7,6,5]. Write a function named transform that takes as arguments list1, list2, r1, and r2, that removes items from list1 in the slice r1:r2, appends them onto list2 in reverse order, and returns the resulting list. For example, in this case, the function call will be tranform(list1, list2, 4, 7).


def get_list():
    a_list = input(
        "Enter elements of list separated by commas: ").strip().split(',')
    return a_list


def get_integer(prompt):
    val = int(input(prompt))
    return val


def transform(list1, list2, index1, index2):
    new_list = []
    for i in list1[index1:index2]:
        new_list.append(i)
    new_list.reverse()

    for i in list1[index1:index2]:
        list1.remove(i)

    for i in new_list:
        list2.append(i)

    return list2, list1


list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)
