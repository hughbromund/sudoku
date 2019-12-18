import numpy

print ("Hello World")

board = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]



if len(board) != 9:
    print("Board is of the wrong dimensions")


# Function to add lines to the Board
def printBoard(board):
    for i in range(0,9):
        print()
        if i % 3 == 0 and i != 0:
            print("----------------")
        for j in range(0,9):
            if j % 3 == 0 and j != 0:
                print(" | ", end = '')
            print(board[i][j], end = '')
    print()
        
        

printBoard(board)