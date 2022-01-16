# Notandi byrjar í reit (1,1)
# Gefa upp hvert notandi getur farið ((N)orth / W(est) / (E)ast / (S)outh)
# Ef notandi framkvæmir aðgerð sem ekki er hægt að gera, prentast út "Not a valid valid_direction!"
# Þegar notandi hefur valið átt sem hægt er að fara, á að gefa upp þá valkosti sem notandi getur tekið næst og svo framvegis.
# Þegar notandi er kominn á endapunkt (3,1), prentast út "Victory!"

pos = [1,1]

while True:
  valid_direction = "N" or "S" or "E" or "W"
  valid_direction = valid_direction.lower()
  
  if pos == [1,1] and valid_direction == True:
    print("You can travel: (N)orth.")
    valid_direction = input("Direction: ")

    if valid_direction == "N":
      pos[1] += 1     # x = 1, y = 2
      print("You can travel: (N)orth or (E)ast or (S)outh.")
      valid_direction = input("Direction: ")
      
      if valid_direction == "N":
        pos[1] += 1   # x = 1, y = 3
        print("You can travel: (E)ast or (S)outh.")
        valid_direction = input("Direction: ")

        if valid_direction == "E":
          pos[0] += 1       # x = 2, y = 3 
          print("You can travel: (W)est or (E)ast.")
          valid_direction = input("Direction: ")

      elif valid_direction == "E":
        pos[0] += 1   # x = 2, y= 2
        print("You can travel: (W)est or (N)orth.")
        valid_direction = input("Direction: ")
      elif valid_direction == "S":
        pos[1] -= 1   # x = 1, y = 1
        print("You can travel: (N)orth.")
        valid_direction = input("Direction: ")
      
    else:
      print("Not a valid valid_direction!")

        

    