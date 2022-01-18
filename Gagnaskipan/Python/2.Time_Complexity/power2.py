

def power(base, exp):
    ret_val = 1
    for i in range(exp):
        ret_val *= base
    return ret_val


print(power(2, 8))


print(2**8)