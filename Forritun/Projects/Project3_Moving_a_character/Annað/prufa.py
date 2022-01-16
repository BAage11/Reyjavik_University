position = int(input("Please chose a starting point between 1 and 10: "))
left = "l"
right = "r"
new_position = position

while position >= 1 and position <= 10:
  if 1 > position < 10 and left == "l":
    new_position -= 1
  elif 1 > positiion < 10 and == "r":
    new_position += 1
  elif position <= 1 or position >= 10:
    new_position += 0
  elif left != "l" or right != "r":
    quit
  