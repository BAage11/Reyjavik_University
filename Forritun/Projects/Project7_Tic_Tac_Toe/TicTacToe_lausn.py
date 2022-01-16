def init_board(dim):
    ''' Returns an initialized board for the given dimension '''
    board = []
    pos = 1

    for _ in range(dim):
        sublist = []
        for __ in range(dim):
            sublist.append(str(pos))
            pos += 1
        board.append(sublist)
    return board

def is_board_filled(board, dim):
    ''' Returns True if all squares of the board have been filled, otherwise False''' 
    for i in range(dim):
        for j in range(dim):
            if board[i][j] != CHAR_X and board[i][j] != CHAR_O:
                return False
    return True

def display_board(board, dim):
    ''' Displays the board position '''
    for i in range(dim):
        for j in range(dim):
            print("{:>5}".format(board[i][j]), end=' ')
        print('')

def get_symbol_for_player(player):
    ''' Returns the appropriate symbol for the given player '''
    return CHAR_X if player == PLAYER_X else CHAR_O

def get_pos_input(symbol):
    ''' Returns an input position entered by player '''
    input_pos = input(symbol + " position: ")
    return input_pos

def is_legal_move(board, dim, row, col):
    ''' Returns true if the given move in (row, col) is legal on the board, otherwise false '''
    if row >= 0 and row < dim and col >= 0 and col < dim: # inside board?
        # Square already occupied?
        if board[row][col] == CHAR_X or board[row][col] == CHAR_O:
            return False
    else:
        return False
    return True

def pos_to_row_col(pos, dim):
    ''' Returns the (col, row) of the given dimension associated with the given integer position '''
    row = (pos-1) // dim
    col = (pos-1) % dim
    return (row, col)

def make_move(board, dim, player):
    ''' Makes a move on the given board of the given dimension for the given player '''
    legal_move = False
    symbol = get_symbol_for_player(player)
    while not legal_move:
        pos = get_pos_input(symbol)
        if pos.isdigit():
            pos = int(pos)
            row, col = pos_to_row_col(pos, dim)
            legal_move = is_legal_move(board, dim, row, col)
            if legal_move:
                 board[row][col] = symbol
        else:
            legal_move = False
        
        if not legal_move:
            print("Illegal move!")

def interpret_result(numO, numX, dim):
    ''' Returns the winner given the number of O's and X's for the given dimension '''
    if numO == dim:
        return PLAYER_O
    elif numX == dim:
        return PLAYER_X
    else:
        return NO_WINNER

def increase_num_Os_Xs(board, row, col, numO, numX):
    ''' Increases number of O's or X's '''
    if board[row][col] == CHAR_O:
        numO += 1
    elif board[row][col] == CHAR_X:
        numX += 1
    
    return (numO, numX)

def check_winner_in_row(board, dim, row):
    ''' Checks for and returns a winner for the given row '''
    numO = 0
    numX = 0

    for j in range(dim):
        numO, numX = increase_num_Os_Xs(board, row, j, numO, numX)

    return interpret_result(numO, numX, dim)

def check_winner_in_column(board, dim, col):
    ''' Checks for and returns a winner for the given column '''
    numO = 0
    numX = 0

    for i in range(dim):
        numO, numX = increase_num_Os_Xs(board, i, col, numO, numX)

    return interpret_result(numO, numX, dim)

def check_diagonals(board, dim):
    ''' Checks for and returns a winner in the two diagonals '''
    numO = 0
    numX = 0
    j = 0

    # From top left to right bottum
    for i in range(dim):
        numO, numX = increase_num_Os_Xs(board, i, j, numO, numX)
        j += 1

    winner =  interpret_result(numO, numX, dim)

    # From top right to left bottom
    if (winner == NO_WINNER):
        numO = 0
        numX = 0
        j = dim-1

        for i in range(dim):
            numO, numX = increase_num_Os_Xs(board, i, j, numO, numX)
            j -= 1
        
        winner = interpret_result(numO, numX, dim)

    return winner

def get_winner(board, dim):
    ''' Returns the winner for the given board if found, else NO_WINNER '''
    # First check for winner in rows
    for i in range(dim):
        winner = check_winner_in_row(board, dim, i)
        if winner != NO_WINNER: 
            return winner

    # Then check for winner in columns
    for j in range(dim):
        winner = check_winner_in_column(board, dim, j)
        if winner != NO_WINNER: 
            return winner

    # Finally, check the diagonals,
    winner = check_diagonals(board, dim)
    return winner


def display_result(winner):
    ''' Prints out the result of the game '''
    if winner == NO_WINNER:
        print("Draw!")
    elif winner == PLAYER_O:
        print("Winner is: " + CHAR_O)
    else:
        print("Winner is: " + CHAR_X)


# Main program starts here
NO_WINNER = -1
PLAYER_O = 0
PLAYER_X = 1
CHAR_O = 'O' 
CHAR_X = 'X'

dim = int(input("Input dimension of the board: "))
board = init_board(dim)
winner = NO_WINNER
display_board(board, dim)

while winner == NO_WINNER and not is_board_filled(board, dim):
    make_move(board, dim, PLAYER_X)
    display_board(board, dim)
    winner = get_winner(board, dim)
    if winner == NO_WINNER and not is_board_filled(board, dim):
        make_move(board, dim, PLAYER_O)
        display_board(board, dim)
        winner = get_winner(board, dim)

display_result(winner)
