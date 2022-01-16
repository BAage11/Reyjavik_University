
def playing_board(board_size):
  """ Make the board for 'Tic-Tac-Toe' playing. """
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
        
def print_board(board):
  """ Printing of the 'Tic-Tac-Toe' game board. """
  for inner_list in playing_board:
        for inner_inner_list in inner_list:
          print("{:>5s}".format(inner_inner_list), end="")
        print()

def player_turns(player):
  """ Check who's turn it is next in the game. """
  playerA = "X"
  playerB = "O"
  if player == playerA:
    player = playerB
    return player
  else:
    player = playerA
    return player

def X_or_O(board, player):
  """ Asks next player for his/her next position on the board, and checks if it is valid (not taken already). """
  position = int(input("{} position: ".format(player)))   
  # Athuga hvort að leikmaður velur tölustaf, ef ekki skilar fallið 'False'.
  for row in range(len(board)):
    for column in range(len(board)):
      if board[row][column] == position:    
      # Ef val leikmanns er á borði, þá...
        board[row][column] = player         
        # ... verður val leikmanns = stafur leikmanns (X eða O) og skilar 'True'
        return True
  return False

def player_choice(board, player):
  """ Check if the game is over - if not, check who's turn it is, and changes the board according to the players position chosen."""
  game_finished = False           # Stopp á lykkju, verður True ef leikur er búinn.
  while game_finished == False:
    next_choice = False           # Stopp á lykkju, verður True ef leikur er búinn.
    next_player = player_turns(player)      # Athuga hvor leikmaður á að gera næst
    while next_choice == False:
      try:    
        next_choice = X_or_O(board, next_player)    
# Athuga hvað leikmaður sem á að gera velur, eða hvort leikmaður velur reit sem er löglegur.
      except:
        print("Illegal move!")
  print_board(board_size)     # prenta uppfært leikborð.


# Main program starts here:
board_size = int(input("Input dimension of the board: "))   # How large the playing board is
playing_board = playing_board(board_size)    
print_board(playing_board)
player_turn = "O"
player_choice(playing_board, player_turn) 