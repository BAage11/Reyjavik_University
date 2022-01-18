

def search(a_list, target):
    index = a_list[len(a_list) // 2]        # tekur index sem er í miðjum listanum

    if len(a_list) == 0:
        return "The list is empty."
    if index == target:
        return "Value found at index {}!".format(index-1)

    elif index > target:                # heldur áfram að leita í efri helming listans
        return search(a_list[:len(a_list) // 2], target)
    elif index < target:                # heldur áfram að leita í neðri helming listans
        return search(a_list[len(a_list) // 2:], target)




a_list = [1,2,3,4,5,6,7,8,9]
print(search(a_list, 6))