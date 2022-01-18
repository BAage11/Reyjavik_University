# Time complexity: O(n)
def power(base, exp):
    ret_val = 1
    for _ in range(exp):
        ret_val *= base
    return ret_val

print(power(2,2))
print(power(3,2))
print(power(2,3))
print(power(2,8))
print(power(4,3))

######################################################

# Time complexity: O(n)
def insert_into_list(a_list, value, index):
    i = len(a_list) - 1
    while i > index:
        a_list[i] = a_list[i-1]
        i -= 1
    a_list[index] = value


list1 = [4,2,6,4,8]
print(list1)
insert_into_list(list1, 3, 2)
print(list1)
