# Print your list to the screen 
# ○ Traverse the list and for each element in the list 
# ■ Print the number to the screen 
# ■ Make the whole list display in one line 
# ■ Separate with both comma and space ● 3, 6, 1, 8, 3 
# ■ Make sure there is not a comma at the end 
# ○ Make a function that does this for you 
# ■ The function can take a list as a parameter 
# ○ What is the time complexity of this operation? 
# ■ Ísl: hver er tímaflækja þessarar aðgerðar? 
# ○ Now you can use this function to test all your other list operations, by outputting the results. 


# Time complexity of this operation: O(n)
def print_list(a_list):
    ret_str = ""
    for i in a_list:
        ret_str += str(i) + ", "
    return ret_str[:-2]


the_list = [0, 2, 8, 4, 6, 8]
print(print_list(the_list))


