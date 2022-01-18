
# Time complex O(n)
def multiply(a, b):
    return_value = 0
    if a <= b:
        for _ in range(a):
            return_value += b
    else:
        for _ in range(b):
            return_value += a
    return return_value

print(multiply(50, 5))
