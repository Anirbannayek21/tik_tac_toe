# global variables
game_is_going = True

# who winner
winner = None

# whos turn
current_player = "X"

# board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
# display board
def display_board():
    print("\n | "+board[0]+" | "+board[1]+" | "+board[2]+" | ")
    print(" | "+board[3]+" | "+board[4]+" | "+board[5]+" | ")
    print(" | "+board[6]+" | "+board[7]+" | "+board[8]+" | \n")

# play game
def play_game():
    global winner
    # display initial board 
    display_board()
    while game_is_going:
        handle_turn(current_player)

        check_game_is_over()

        flip_player()

# the game is over 
    if winner=="X" or winner== "O" :
        print(winner + " win the game.")
    elif winner == None:
        print("the game is tie.")


# handle turn
def handle_turn(current_player):
    print(current_player + "'s turn")
    position = input("\nChoose a position from 1-9:")
    valid = False
    while not valid:
        while position not in["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9:")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("invalid move")
    board[position] = current_player
    display_board()

# flip player 
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def check_game_is_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    #check rows
    row_winner = check_row()
    #check colums
    colums_winner = check_colums()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif colums_winner:
        winner = colums_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return winner

def check_row():
    global game_is_going

    row_1 =  board[0]==board[1]==board[2] != "-"
    row_2 = board[3]==board[4]==board[5] != "-"
    row_3 = board[6]==board[7]==board[8] != "-"
    if row_1 or row_2 or row_3:
        game_is_going = False
    if  row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_colums():
    global game_is_going

    col_1 = board[0]==board[3]==board[6] != "-"
    col_2 = board[1]==board[4]==board[7] != "-"
    col_3 = board[2]==board[5]==board[8] != "-"
    if col_1 or col_2 or col_3:
        game_is_going = False
    if  col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_is_going

    dia_1 = board[0]==board[4]==board[8] != "-"
    dia_2 = board[2]==board[4]==board[6] != "-"
    if dia_1 or dia_2 :
        game_is_going = False
    if  dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    return
#check tie or not ,if tie the game will stop
def check_if_tie():
    global game_is_going
    if "-" not in board:
        game_is_going = False
    return

play_game()


