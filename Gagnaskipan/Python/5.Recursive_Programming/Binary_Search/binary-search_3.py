a_list = [0, 2, 4, 6, 8]

def binary_search(a_list, target, low, high):
    mid = (low + high) // 2

    if low > high:
        return "Value not found in the list."
    if a_list[mid] == target:
        return "The value search can be found at index: {}".format(mid)
    elif a_list[mid] > target:
        return binary_search(a_list,target, low, mid-1)
    elif a_list[mid] < target:
        return binary_search(a_list,target, mid+1, high)
    

lengthoflist = (len(a_list)) - 1
print(binary_search(a_list, 7, 0, lengthoflist))


print((0+7) % 2)