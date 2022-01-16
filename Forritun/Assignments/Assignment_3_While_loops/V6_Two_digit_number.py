# Write a program using a while statement, that prints out the two-digit number such that  when you square it, the resulting three-digit number has its rightmost two digits the same as the original two-digit number.  That is, for a number in the form AB:
# AB * AB = CAB, for some C. 

x = 10
y = 99

while x <= y:
  C = x**2
  if x == C % 100:
  # Cut-tar af og skilur eftir tvo öftustu tölustafina úr útkomunnni
    print(x)
    break
  x += 1
