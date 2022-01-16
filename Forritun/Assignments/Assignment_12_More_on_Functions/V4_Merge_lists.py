# Question 4: Merge lists
# Write a function merge_lists that takes two lists as arguments, merges them into a third list without duplicates and returns the third list sorted. 
# The elements of each list are strings.

def merge_lists(list1, list2):
  list3 = list1 + list2
  list3_new = []
  for i in list3:
    if i not in list3_new:
      list3_new.append(i)
  
  list3_new.sort()
  return list3_new


# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
