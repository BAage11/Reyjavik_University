#Time complexity 0(n)
import random

def switch_items(the_list,size):
    rand_num = random.randint(0,size-1)
    place_holder = the_list[rand_num]
    the_list[rand_num] = the_list[rand_num+1]
    the_list[rand_num+1] = place_holder
    return the_list
 

def switch_two_items(the_list,size):
    rand_num1 = random.randint(0,size-1)
    rand_num2 = random.randint(0,size-1)

    place_holder = the_list[rand_num1]
    the_list[rand_num1] = the_list[rand_num2]
    the_list[rand_num2] = place_holder
    return the_list

    
the_list = [1,2,3,4,5,6]
size = len(the_list)
print(switch_items(the_list,size))
the_list = [1,2,3,4,5,6]
print(switch_two_items(the_list,size))