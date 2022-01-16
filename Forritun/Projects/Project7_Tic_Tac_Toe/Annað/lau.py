board = []

# Creates the board and the size of the board
def create_board(board_size):
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

# Check if select number exists
def check_if_number_exists(number):
  number_exists = False
  for key, value in enumerate(board):
    if str(number) in value:
      number_exists = True
  return number_exists

# Modify the board based on player selection
def modify_board(number, player):
  player_str = str(player).upper()
  number_str = str(number)
  for key_board, value_board in enumerate(board):
    for key_line, value_line in enumerate(value_board):
      if value_line == number_str:
        board[key_board][key_line] = player_str

# Check each row if there is a win
def check_row_winner(player):
  winner = False
  for x in range(len(board)):
    counter_row = 0
    for y in range(len(board)):
      if board[x][y] == player:
        counter_row += 1
        if counter_row == len(board):
          winner = True
        continue
  return winner

# Checks columns down if there is a win
def check_col_winner(player):
  winner = False
  for x in range(len(board)):
    counter_col = 0
    for y in range(len(board)):
      if board[y][x] == player:
        counter_col += 1
        if counter_col == len(board):
          winner = True
        continue
  return winner

# Checks diagonal rows from left to right
def check_dia_winner_lr(player):
  winner = False
  counter_dia = 0
  for x in range(len(board)):
    if board[x][x] == player:
      counter_dia += 1
      if counter_dia == len(board):
        winner = True
  return winner

# Checks diagonal rows from right to left
def check_dia_winner_rl(player):
  winner = False
  counter_dia = 0
  reverse_count = 0
  for x in reversed(range(len(board))):
    if board[x][reverse_count] == player:
      counter_dia += 1
      reverse_count += 1
    if counter_dia == len(board):
      winner = True
  return winner

# Check if draw
def check_draw():
  number_exists = False
  for value_board in board:
    for value_line in value_board:
      try:
        if int(value_line):
          number_exists = True
      except ValueError:
        pass
  return number_exists

# Evaluates the board and then figures out who is the winner
# Returns two variables, eather if there is a draw or if there is a winner.
def check_winner_board(player):
  is_winner = False
  is_draw = False
  if check_row_winner(player) == True or check_col_winner(player) == True or check_dia_winner_lr(player) == True or check_dia_winner_rl(player) == True:
    is_winner = True
  else:
    is_winner = False
  if is_winner == False:
    if check_draw() == False:
      is_draw = True
  return is_winner, is_draw

# Prints out the board
def print_out_board():
  for line in range(len(board)):
    lines = "{:>5}"*len(board)
    print(lines.format(*board[line]))

# Allows the player to turn
def player_turn(player):
  while True:
    number = input("{} position: ".format(player))
    if check_if_number_exists(number) == True:
      modify_board(number,player)
      if player == "X":
        player = "O"
      else:
        player = "X"
      break
    else:
      print("Illegal move!")
  return player

# Main application
def main():
  board_size = int(input("Input dimension of the board: "))
  create_board(board_size)
  player = "X"
  while True:
    x_won, draw = check_winner_board("X")
    o_won, draw = check_winner_board("O")
    if x_won == True:
      print_out_board()
      print("Winner is: X")
      break
    if o_won == True:
      print_out_board()
      print("Winner is: O")
      break
    if draw == True:
      print_out_board()
      print("Draw!")
      break
    print_out_board()
    player = player_turn(player)

main()
