
def playing_board(board_size):
  choices = []
  for x in range(0, int(board_size)**2):
    choices.append(x+1)
  board = []
  for i in range(board_size):
    string = ""
    for j in range(board_size):
      string += str(choices[(i*board_size)+j]) + " "
    board.append(string[:-1].split())
  return board
        
def validOrInvalid(choice, playing_board):  
  try:
    for rows in playing_board:
      if choice in rows:
        return True
  except ValueError:
    print("Illegal move!")
    return False  

def playerA(playing_board):
  choice = int(input("X position: "))
  if validOrInvalid(choice, playing_board) is True:
    for rows in playing_board:
      for index, items in enumerate(rows):
        if choice == items:
          rows[index] = "X"
          return playing_board

def playerB(playing_board):
  choice = int(input("O position: "))
  if validOrInvalid(choice, playing_board) is True:
    for rows in playing_board:
      for index, items in enumerate(rows):
        if choice == items:
          rows[index] = "O"
          return playing_board

def print_board():
  for inner_list in playing_board:
        for inner_inner_list in inner_list:
          print("{:>5s}".format(inner_inner_list), end="")
        print()


board_size = int(input("Input dimension of the board: "))
playing_board = playing_board(board_size)
print_board()
      
victory = False
while victory != True:
  player_one = playerA(playing_board)
  print_board()
  player_two = playerB(playing_board)
  print_board()