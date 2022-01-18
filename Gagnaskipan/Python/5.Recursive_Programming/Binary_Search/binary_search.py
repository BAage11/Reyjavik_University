# Binary search 
# ○ Implement binary search in an ordered list using recursive programmin

def search(a_list, target, low, high):
    low = a_list[0]
    high = a_list[-1]

    if len(a_list) == 0:
        return False

    if target == a_list[0] or a_list[-1] == target:
        return True
    else:
        mid = int((high-low) / 2)
        
        if a_list[mid] == target:
            return True
        elif a_list[mid] > target:
            low = mid
            return search(a_list[:mid-1], target, low, mid)
        elif a_list[mid] < target:
            high = mid
            return search(a_list[mid+1:], target, mid, high)

the_list = [0, 2, 4, 6, 8, 10]
print(search(the_list, 8, 0, len(the_list)))