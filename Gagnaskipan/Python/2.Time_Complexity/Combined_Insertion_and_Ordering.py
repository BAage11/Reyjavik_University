from random import randint
# Full time complex O(n^2)

def random_list(list_to_random):
    for i in range(len(list_to_random)):
        list_to_random[i] = randint(1, 6)
    return list_to_random

# Time complexity O(n)
def order_number(lst, number):
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

# Time complexity O(n)
def order_full(lst):
    new_lst = []
    new_lst.append(lst[0])
    for x in lst:
        new_lst = order_number(new_lst, x)
    return new_lst

# Make a random list
randm_list = random_list([0]*20)

# Sort it using our method.
lst = order_full(randm_list)
print(lst)