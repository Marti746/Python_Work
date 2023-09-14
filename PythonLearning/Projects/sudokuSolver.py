# A sudoku Solver that will take in a unfinihsed board and solve it
def printBoard(bo):
    for c in range(len(bo)):
        # Checks to see if the column is three and prints a line to seperate it
        if c % 3 == 0 and c != 0:
            print("------------")
            # loops through the rows
        for r in range(len(bo[c])):
            # checks to see if it is 3x3 to print vertical row
            if r % 3 == 0 and r != 0:
                print("|", end="")
            if r == 8:
                print(bo[c][r])
            else:
                print(str(bo[c][r]) + " ",end="")

# Function to find empyt spots in the board
def findEmpty(bo):
    for c in range(len(bo)):
        for r in range(len(bo[c])):
            # change to period (.) later
            if bo[c][r] == 0: 
                return (c, r)
    return None

def valid(bo, num, pos):
    # Check if the number has occured within the row
    for r in range(len(bo)):
        if bo[pos[0]][r] == num and pos[1] != r:
            return False
    # Check if it is in the column
    for c in range(len(bo)):
        if bo[c][pos[1]] == num and pos[0] != c:
            return False
    # Check to see if it has occured in grid
    gridX = pos[1] // 3
    gridY = pos[0] // 3
    for i in range(gridY*3, gridY*3 + 3):
        for j in range(gridX*3, gridX*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

# Solving the sudoku board
def solveBoard(bo):
    find = findEmpty(bo)
    if not find:
        # Came back Null meaning its solved
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            # Insert num into the row and col
            bo[row][col] = i
            # Recall solve for next one
            if solveBoard(bo):
                return True
            # Error we backtrack and put in a 0
            bo[row][col] = 0
    return False
# Change to have it be user input
board=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]

# Call functions
printBoard(board)
solveBoard(board)
print("Solving")
print("\nSolved Sudoku Boared")
printBoard(board)