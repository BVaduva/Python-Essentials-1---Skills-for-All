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


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    free_fields = []

    for row in board:  # Iterate over each row in the board
        for col in row:  # Iterate over each column in the row
            if col != 'X' and col != 'O':  # Check if the cell is not occupied
                free_fields.append(col)  # Append the free field to the list
    if len(free_fields) == 0:
        print("It's a Draw")
        return None

    return free_fields # Return the list of free fields


def enter_move(board):
    valid_input = False

    while not valid_input:
        try:
            move = int(input("Enter your move: "))  # Example move, replace with input("Enter your move: ")
            if move < 1 or move > 9: #limit user input to the boards numbers
                raise ValueError("Invalid entry! Please enter a number between 1 and 9.")
            
            free_fields = make_list_of_free_fields(board) #update free_fields
            if move in free_fields: #check if the entered field number is free
                for row in range(len(board)): #len(board) is 3, range(len(board)) generates the sequence [0, 1, 2]
                    for col in range(len(board[row])):
                        if move == board[row][col]: #check if the entered move is equal to a free field at place [row][col] ex. [1][1], which would be 4
                            # Update the value at the specified row and column indices
                            board[row][col] = 'O'         
                            valid_input = True
                            display_board(board)
                            return board  # Return the updated board
        except ValueError as ve:
            print(ve)
        except:
            print("Wrong Input")


def draw_move(board):
    # The function draws the computer's move and updates the board.
    valid_input = False

    while not valid_input:
        move = randint(1,9)
        free_fields = make_list_of_free_fields(board)
        if move in free_fields: #check if the entered field number is free
            for row in range(len(board)): #len(board) is 3, range(len(board)) generates the sequence [0, 1, 2]
                for col in range(len(board[row])):
                    if move == board[row][col]: #check if the entered move is equal to a free field at place [row][col] ex. [1][1], which would be 4
                        # Update the value at the specified row and column indices
                        board[row][col] = 'X'
                        print(f"CPU entered: {move}")                
                        valid_input = True
                        display_board(board)

    return board


def victory_for(board, sign):
    # Analyzes the board's status in order to check if a win is possible
    if (sign != board[0][0] and
        sign != board[1][1] and
        sign != board[2][2]):         
        return None
    
    # Check row
    for row in range(len(board)):
        counter = 0
        if sign != board[row][row]:
            continue
        else:
            for ele in board[row]:
                if sign == ele:
                    counter += 1
                    if counter == 3:
                        return True

    # Check col
    if sign in board[0]:
        index = board[0].index(sign)
        counter = 0
        for col in range(len(board)): 
            if sign == board[col][index]:
                counter += 1
                if counter == 3:
                    return True
            
    # Check diagonal
    if ('X' == board[0][0] and
        'X' == board[1][1] and
        'X' == board[2][2]):
        return True
    
    # Check anti-diagonal
    if ('X' == board[0][2] and
        'X' == board[1][1] and
        'X' == board[2][0]):
        return True



board = [
  [1, 2, 3],
  [4,'X',6],
  [7, 8, 9]
]

sign = 'X'
free_fields = make_list_of_free_fields(board)
winner = False

display_board(board)
while not winner:

    enter_move(board)
    sign = 'O'

    if victory_for(board, sign):
        print("You Won!")
        winner = True
        break

    make_list_of_free_fields(board)

    draw_move(board)
    sign = 'X'

    if victory_for(board, sign):
        print("You Lost :( ")
        winner = True
        break

    make_list_of_free_fields(board)


