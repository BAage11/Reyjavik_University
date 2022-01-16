
# https://github.com/BenjaminAage/TileTraveller/blob/master/tile_traveller_def.py
# 1. Which implementation was easier and why? 
#    - It was quite hard to implement program #1 (without functions), as you had to figure out
#      all the factors to have the program up and running. However, the function program (#2) was
#      not easier to be fully honest, but on the other hand it is much more readable and
#      easiser to understand afterwards.
# 2. Which implementation is more readable and why?
#    - As stated in answer number 1, the second program is easier to understand as you are
#      dividing the overall problem into smaller sectors. Thereby making it more readable.
# 3. Which problems in the first implementations were you able to solve 
#    with the latter implementation?
#    - To categories the print operations of the program, so when the user of the program
#      has entered a valid direction, the program gives the next direction easily without
#      writting the code again (def printed(route)).
#      With that, you could make another function that defines what the user types in, and
#      thereby return the direction he/she wants to go next.
#      All that was left to do then, is to create the while-loop to run the program sufficiently,
#      as well as to use the functions created within the loop.
# 
#     
def new_route(x, y):
  if x == 1 and y == 1:
    return "N"
  elif x == 1 and y == 2:
    return "NES"
  elif x == 1 and y == 3:
    return "ES"
  elif x == 2 and y == 1:
    return "N"
  elif x == 2 and y == 2:
    return "SW"
  elif x == 2 and y == 3:
    return "EW"
  elif x == 3 and y == 1:
    return ""
  elif x == 3 and y == 2:
    return "NS"
  elif x == 3 and y == 3:
    return "SW"


def routes(direction, route):
  for i in route:
    if i == direction:
      return True
  return False


def printed(route):
  if route != "":
    print("You can travel: ", end="")

    for i in range(len(route)):
      if i != 0:
        print(" or ", end="")
      if route[i] == "N":
        print("(N)orth", end="")
      elif route[i] == "E":
        print("(E)ast", end="")
      elif route[i] == "S":
        print("(S)outh", end="")
      elif route[i] == "W":
        print("(W)est", end="")
    print(".")


x = 1
y = 1
start = "N"
print("You can travel: (N)orth.")

while not (x == 3 and y == 1):
  direction = input("Direction: ").upper()
  if routes(direction, start):
    if direction == "N":
      y += 1
    if direction == "E":
      x += 1
    if direction == "S":
      y -= 1
    if direction == "W":
      x -= 1

    start = new_route(x, y)
    printed(start)
  else:
      print("Not a valid direction!")
      

print("Victory!")


