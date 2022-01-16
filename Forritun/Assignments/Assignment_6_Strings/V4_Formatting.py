# Given input that represents a floating point number, that is, made up of digits and at least one decimal point, convert the input to a float and print it with the following specifications:
# * field width of 12
# * 2 decimal digits of precision
# * right justified
 
# For example, if the input is
# 1234.56789
# The output will be
     # 1234.57
# Note the five spaces to the left of the digit 1.

s = float(input("Input a float: "))
print("{:>12.2f}".format(s))