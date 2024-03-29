import numpy as np
from appJar import gui
import math

print ("Hello World")

board = np.array([[1,2,3,4,5,6,7,8,9],
        [2,3,4,5,6,7,8,9,1],
        [3,4,0,0,0,0,0,0,0],
        [4,5,0,0,0,0,0,0,0],
        [5,6,0,0,0,0,0,0,0],
        [6,7,0,0,0,0,0,0,0],
        [7,8,0,0,0,0,0,0,0],
        [8,9,0,0,0,0,0,0,0],
        [9,1,0,0,0,0,0,0,0],])

correctBoard = np.array([[3,7,9,2,4,5,8,6,1],
        [2,8,5,3,6,1,9,7,4],
        [1,6,4,9,7,8,2,3,5],
        [9,5,8,6,3,4,1,2,7],
        [4,3,7,1,9,2,6,5,8],
        [6,2,1,8,5,7,4,9,3],
        [7,9,2,4,1,3,5,8,6],
        [8,4,3,5,2,6,7,1,9],
        [5,1,6,7,8,9,3,4,2]])

starterBoard = np.array([[5,3,0,0,7,0,0,0,0,],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]])

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

# Takes in a Sudoku Board and checks if it is solved
# in a valid way
def checkBoard(board):
    # Check if the rows contain 1-9 without repetition
    for row in board:
        # print("Checking rows")
        check = [0,0,0,0,0,0,0,0,0]
        for value in row:
            if value <= 0 or value > 9:
                print("The board has invalid entries")
                return False
            # If the value has already appeared we return false
            if check[value - 1] == 1:
                print("A value was duplicated in the Row")
                print(check)
                return False
            # If this is the first time finding the value we update the array
            if check[value - 1] == 0:
                check[value - 1] = 1

    # Check if the columns contain 1-9 without repetition
    transpose = board.T
    for row in transpose:
        # print("Checking Column")
        check = [0,0,0,0,0,0,0,0,0]
        for value in row:
            if value <= 0 or value > 9:
                print("The board has invalid entries")
                return False
            # If the value has already appeared we return false
            if check[value - 1] == 1:
                print("A value was duplicated in the Column")
                print(check)
                return False
            # If this is the first time finding the value we update the array
            if check[value - 1] == 0:
                check[value - 1] = 1
    # Check if the 3x3 squares contain 1-9 without repetition
    for i in range(0,3):
        for j in range(0,3):
            starCol = 3 * i
            startRow = 3 * j
            check = [0,0,0,0,0,0,0,0,0]
            for k in range(starCol, starCol + 3):
                for l in range(startRow, startRow + 3):
                    value = board[k][l]
                    if value <= 0 or value > 9:
                        print("The board has invalid entries")
                        return False
                    # If the value has already appeared we return false
                    if check[value - 1] == 1:
                        print("A value was duplicated in the 3x3 area")
                        print(check)
                        return False
                    # If this is the first time finding the value we update the array
                    if check[value - 1] == 0:
                        check[value - 1] = 1 
    return True


def press(button):
    if button == "Check Board":
        test = app.getAllEntries()
        array = np.zeros((9,9))
        # Take in all the Data from the game board
        for col in range(0,9):
            for row in range(0,9):
                if starterBoard[col][row] != 0:
                    array[col][row] = starterBoard[col][row]
                else:
                    entry = app.getEntry(str(col)+str(row))
                    if entry is None:
                        array[col][row] = 0
                    else:
                        array[col][row] = entry
        
        array = array.astype(int)
        print(array)
        print(checkBoard(array))

app=gui("Sudoku", "1000x1000")
app.setBg("white")
# news means North East West South. It keeps the content centered in the cell

app.setExpand("both")
app.setStretch("both")
app.setSticky("news")
app.setPadding([0,0])
app.setFont(15)
for col in range(0,11):
    for row in range(0,11):
        if col == 3:
            app.addVerticalSeparator(row=row,column=col, rowspan = 0, height = 1)
        if col == 7:
            app.addVerticalSeparator(row=row,column=col, rowspan = 0)
        if row == 3:
            app.addHorizontalSeparator(row=row,column=col, colspan = 0)
        if row == 7:
            app.addHorizontalSeparator(row=row,column=col, colspan = 0)

"""
app.addHorizontalSeparator(row=3,column=0,colspan=11,rowspan=1)
app.addHorizontalSeparator(row=7,column=0,colspan=11,rowspan=1)
app.addVerticalSeparator(row=0,column=3,colspan=1,rowspan=11)
app.addVerticalSeparator(row=0,column=7,colspan=1,rowspan=11)
"""

#app.setPadding(20,20)
# Setup all of the Entry boxes

for col in range(0,9):
    for row in range(0,9):
        colLocation = col
        rowLoaction = row
        if col == 3:
            app.addVerticalSeparator(row=row,column=col, rowspan = 0)
        if col == 7:
            app.addVerticalSeparator(row=row,column=col, rowspan = 0)
        if row == 3:
            app.addHorizontalSeparator(row=row,column=col, colspan = 0)
        if row == 7:
            app.addHorizontalSeparator(row=row,column=col, colspan = 0)

        if col >= 3:
            colLocation = colLocation + 1
        if col >= 6:
            colLocation = colLocation + 1
        if row >= 3:
            rowLoaction = rowLoaction + 1
        if row >= 6:
            rowLoaction = rowLoaction + 1
        print(colLocation, rowLoaction)
        if starterBoard[col][row] == 0:
            app.addNumericEntry(str(col)+str(row), colLocation, rowLoaction)
        else:
            app.addLabel(str(col)+str(row), str(starterBoard[col][row]), colLocation, rowLoaction)

# Add the final button to Check the Board

app.addButton("Check Board", press, 11, 0, 11,1)
app.go()