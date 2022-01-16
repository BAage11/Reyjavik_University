def get_list(length):
  """ Nested list from input-size of board from user. """
  row = 0
  ticlist = []
  while length >= 3 and row < length: 
    line_list =[]
    for x in range(length):
      x = x + 1
      formula = (x) + (length * row)
      line_list.append(str(formula))
      if x == length:
        break
    ticlist.append(line_list)
    row += 1
  return ticlist

def board_print(ticlist):
  """ Prints the board in the right format. """
  for inner_list in ticlist:
      for inner_inner_list in inner_list:
          print("{:>6s}".format(inner_inner_list), end="")
      print()

def find_player(player):
  """ Rotation of the players, changes who's turn it is. """
  playerA = "X"
  playerB = "O"
  if player == playerA:
    player = playerB
  else:
    player = playerA
  return player

def player_XO(ticlist, player):
  """ Asks the user what position he/she wants to take on the board and marks that position on the board with the players mark (X or O). """
  position = str(input("{} position: ".format(player)))
  if player == "X":
    for rows in ticlist:
      for index, items in enumerate(rows):
        if position in items:
          rows[index] = "X"
          return ticlist
  if player == "O":
    for rows in ticlist:
      for index, items in enumerate(rows):
        if position in items:
          rows[index] = "O"
          return ticlist
    
def victory(ticlist, length):   
  # Missing code....
  victory = False
  return victory


# Main program starts here:
length = int(input('Input dimension of the board: '))
ticlist = get_list(length)
board_print(ticlist)

next_player = "O"
victory = victory(ticlist, length)
while victory == False:
  next_player = find_player(next_player)
  player_choice = player_XO(ticlist, next_player)
  board_print(ticlist)
  
