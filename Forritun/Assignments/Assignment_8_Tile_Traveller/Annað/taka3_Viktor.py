# prenta mögulegar áttir  
# annars:  
# prenta Invalid 
# prenta Sigur 
  
x = 1 
y = 1 
leidir = "N" 

print("You can travel: (N)orth.") 

while True: 
  x2 = x 
  y2 = y 
  inntak = input("Direction: ").upper() 

  for i in leidir: 
    if i == inntak: 
      if inntak == "N": 
        y += 1 
      elif inntak == "E": 
        x += 1 
      elif inntak == "S": 
        y -= 1 
      elif inntak == "W": 
        x -= 1 
      break 
  else: 
    print("Not a valid direction!") 

  if x2 != x or y2 != y: 
    if x == 1 and y == 1: 
      leidir = "N" 
    elif x == 1 and y == 2: 
      leidir = "NES" 
    elif x == 1 and y == 3: 
      leidir = "ES" 
    elif x == 2 and y == 1: 
      leidir = "N" 
    elif x == 2 and y == 2: 
      leidir = "SW" 
    elif x == 2 and y == 3: 
      leidir = "EW" 
    elif x == 3 and y == 1: 
      break 
    elif x == 3 and y == 2: 
      leidir = "NS" 
    elif x == 3 and y == 3: 
      leidir = "SW" 
    print("You can travel: ", end="") 

    for i in range(len(leidir)): 
      if i != 0: 
        print(" or ", end="") 
      if leidir[i] == "N": 
        print("(N)orth", end="") 
      elif leidir[i] == "E": 
        print("(E)ast", end="") 
      elif leidir[i] == "S": 
        print("(S)outh", end="") 
      elif leidir[i] == "W": 
        print("(W)est", end="") 
    print() 

print("Victory!")