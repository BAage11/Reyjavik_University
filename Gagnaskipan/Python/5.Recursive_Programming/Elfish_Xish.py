
def x_ish(a_str, x):
    """ Outer Loop """
    if x == "":
        return True

    if(x_ish_letter(a_str,x[0])):
        return x_ish(a_str, x[1:])
    else: 
        return False

def x_ish_letter(a_str, x):
    """ Inner Loop """
    if a_str == "":
        return False

    if(a_str[0] == x):
        return True
    else:
        return x_ish_letter(a_str[1:], x)



print(x_ish("gagnaskipan", "a"))       # -> True 
print(x_ish("gagnaskipan", "gnask"))   # -> True 
print(x_ish("gagnaskipan", "iganpsk")) # -> True 
print(x_ish("gagnaskipan", "gnAsk"))   # -> False 
print(x_ish("gagnaskipan", "gnesk"))   # -> False
