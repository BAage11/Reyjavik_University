from random import randint

# Time complexity O(n)
def order(lst, number):
    # If number is the bigger than the last number from list
    if lst[len(lst) - 1] <= number:
        lst.append(number)
    else:
        lst.append(number) # O(1)
        temp_store = 0
        for x in range(0, len(lst)):
            if lst[x] > number and temp_store == 0:
                temp_store = lst[x]
                lst[x] = number
            elif temp_store != 0:
                a = temp_store
                temp_store = lst[x]
                lst[x] = a
    return lst

# TEST CASES

# Make a random list
lst = []
for x in range(0, 50):
    lst.append(randint(0, 7000))
lst.sort() # Sort that lists

# Debugging
print(lst)
a = randint(1, 6)
print("Appending: " + str(a))

# Use the function
ordered_list = order(lst, a)
print(ordered_list)