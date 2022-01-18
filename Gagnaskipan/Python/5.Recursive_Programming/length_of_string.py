# ● Length of string 
# ○ Implement a recursive function that calculates the length of a string 
# ○ Takes a string as a parameter 
# ○ Returns an integer (+1 for each character)

def length(string):
    if len(string) == 0:
        return 0
    return (1 + length(string[1:]))

print(length("blablabla"))