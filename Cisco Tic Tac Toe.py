from random import randint

def display_board(board):
    # The function accepts one parameter containing the board's current status
    board = [
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
    #draw the board
    for line in board:
        print(line)

    return board


def enter_move(board):
    valid_input = False
    global move_count

    while not valid_input:
        try:
            print("Enter your move: ")#
            move = 4  # Example move, replace with input("Enter your move: ")
            if move < 1 or move > 9: #limit user input to the boards numbers
                raise ValueError("Invalid entry! Please enter a number between 1 and 9.")
            
            free_fields = make_list_of_free_fields(board) #update free_fields
            if move in free_fields: #check if the entered field number is free
                for row in range(len(board)): #len(board) is 3, range(len(board)) generates the sequence [0, 1, 2]
                    for col in range(len(board[row])):
                        if move == board[row][col]: #check if the entered move is equal to a free field at place [row][col] ex. [1][1], which would be 4
                            # Update the value at the specified row and column indices
                            board[row][col] = 'O'
                            move_count += 1           
                            valid_input = True
                            display_board(board)
                            return board  # Return the updated board
        except ValueError as ve:
            print(ve)
        except:
            print("Wrong Input")



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    free_fields = []

    for row in board:  # Iterate over each row in the board
        for col in row:  # Iterate over each column in the row
            if col != 'X' and col != 'O':  # Check if the cell is not occupied
                free_fields.append(col)  # Append the free field to the list

    return free_fields # Return the list of free fields

def victory_for(board, sign):
    counter = 0
    # The function analyzes the board's status in order to check if
    for row in range(len(board)):
        for col in range(len(board[row])):
            if sign == board[row][col]:
                counter += 1
                if counter == 3:
                    winner = True
                    return winner
                continue

    # the player using 'O's or 'X's has won the game
    return print(f"{sign} * {counter}")

def draw_move(board):
    # The function draws the computer's move and updates the board.
    valid_input = False
    global move_count_cpu

    while not valid_input:
        move = randint(1,9)
        free_fields = make_list_of_free_fields(board)
        if move in free_fields: #check if the entered field number is free
            for row in range(len(board)): #len(board) is 3, range(len(board)) generates the sequence [0, 1, 2]
                for col in range(len(board[row])):
                    if move == board[row][col]: #check if the entered move is equal to a free field at place [row][col] ex. [1][1], which would be 4
                        # Update the value at the specified row and column indices
                        board[row][col] = 'X'
                        move_count_cpu += 1
                        print(f"CPU entered: {move}")                
                        valid_input = True
                        display_board(board)

    return board

board = [
  [1, 2, 3],
  [4,'X',6],
  [7, 8, 9]
]

free_fields = make_list_of_free_fields(board)
move_count = 0
move_count_cpu = 1
winner = False
sign = 'X'

victory_for(board, sign)
display_board(board)
enter_move(board)
draw_move(board)

