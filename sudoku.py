NUM_ROWS = 9
NUM_COLUMNS = 9
game_board = [
    [4,0,0,9,0,5,8,1,0],
    [9,1,0,0,0,0,7,0,5],
    [0,0,0,0,1,6,3,0,4],
    [0,2,1,6,0,4,0,8,0],
    [5,9,0,0,8,1,6,0,0],
    [6,7,0,5,0,0,0,0,0],
    [1,0,0,0,0,0,9,0,0],
    [2,3,0,8,0,0,1,0,6],
    [7,0,0,1,5,0,0,3,8]
]

# Print out game board
def show_board(board):
    for i in range (NUM_ROWS):
        if (i % 3 == 0) and (i > 0): 
            print ("- - - - - - - - - - - - ") # For every 3 rows add a divider

        for j in range (NUM_COLUMNS):
            if (j % 3 == 0) and (j > 0): # For every 3 columns add a divider
                print (" | ", end = "") # Place a space after string instead of a newline

            if j == 8:
                 print (board[i][j])
            else:
                print (str (board[i][j]) + " ", end = "") # Place a space after string instead of a newline

# Returns the location of the first empty square found. If all spaces are filled, returns false.
def find_empty_square(board):
    for i in range (NUM_ROWS):
        for j in range (NUM_COLUMNS):
            if board[i][j] == 0: 
                return (i,j) # Return location as tuple (row #, column #)
    return False 

# Checks if a board is valid
def valid_board(board, val, location):

    # Check to see if a row is valid
    for i in range (NUM_COLUMNS):
        if board[location[0]][i] == val and location[1] != i: # If val is already found in row, return False
            return False

    #Check to see if a column is valid
    for i in range (NUM_ROWS):
        if board[i][location[1]] == val and location[0] != i: #If val is already found in row, return False
            return False

    #Check to see if a square is valid
    box_x = location[1] // 3
    box_y = location[0] // 3

    for i in range (box_y * 3, box_y * 3 + 3): # Identifying which of the 9 boxes to search in
        for j in range (box_x * 3, box_x * 3 + 3):
            if board[i][j] == val and location != (i,j):
                return False #If value is already found in square, return False

    return True # If number placement is valid, return True


# Solve the sudoku board using backtracking
def solve_board(board):
    empty_space = find_empty_square(board)
    if not empty_space: 
        return True #If all the spots on the board are filled, a solution was found.
    else:
        (row,col) = empty_space # Location of empty space
    
        for num in range (1, NUM_COLUMNS + 1):
            if valid_board(board, num, empty_space):
                board[row][col] = num # If valid, add value to board

                if solve_board(board):
                    return True

                board[row][col] = 0 # If not valid, reset value back to 0 and backtrack. Continue trying other numbers.

    return False


# Display original sudoku board
print ("______________________")
print ("Original Board:")
show_board(game_board)

# Display solved sudoku board
solve_board(game_board)
print ("______________________")
print ("Solved Board:")
show_board(game_board)
