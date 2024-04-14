from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    board_current = [
    "+-------+-------+-------+",
    "|       |       |       |",
    f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |",
    "|       |       |       |",
    "+-------+-------+-------+",
    "|       |       |       |",
    f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |",
    "|       |       |       |",
    "+-------+-------+-------+",
    "|       |       |       |",
    f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |",
    "|       |       |       |",
    "+-------+-------+-------+"
]
    for line in board_current:
        print(line)

    return "Current Board"
    #return int(input("Enter your move: "))
    


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    board_current = board
    move = int(input("Enter your move: ")) 
    # checks the input, and updates the board according to the user's decision.
    valid_input = False
    while valid_input == False:
        try:
            move = int(input("Enter your move: "))
        except:
            print("Wrong Input")


    
    return 0

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    free_field = [] 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return 0

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    return 0

def draw_move(board):
    # The function draws the computer's move and updates the board.
    return 0

board = [
  [1, 2, 3],
  [4,'X',6],
  [7, 8, 9]
]

print(display_board(board))
