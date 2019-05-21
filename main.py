from turtle import *
import time
#TODO: Add turtle implementation for clicking/typing spaces
baseX = -75
baseY = -75
gridlength = 50
boardState = [[0,0,0],[0,0,0],[0,0,0]]
buttonStr = ["Play Again", "Exit"]
buttonLoc = []
al = Turtle()
al.shape("turtle")
screen = Screen()
al.speed(7)
playerOneTurn = True
gameOver = False
errorText = ""

def createBoard():
    gameOver = False
    for x in range (3):
        for y in range (3):
            __createBox(x, y)
    __createLabels()
    __createButtons()
    whoseTurn()

'''
* Creating a box at (col, row) location
* @param 
'''
def __createBox(col, row):
    x = baseX + (col * 50)
    y = baseY + (row * 50)
    al.up()
    al.goto(x, y)
    al.down()
    al.seth(90)
    for i in range(4):
        al.forward(gridlength)
        al.right(90)
    al.up()
    al.goto(x + (gridlength / 2), y + (gridlength / 2.5))
    al.down()
    al.write(str((col + 1) + (row * 3)))
    al.up()

def __createLabels():
    """Creates the labels for whose turn it is"""
    al.up()
    al.goto(0, baseY - (gridlength * 2))
    al.write("Whose Turn Is It?", False, align="center")
    al.goto(0, baseY - (gridlength * 2.25))
    al.down()
    al.seth(270)
    al.forward(gridlength * 2)
    al.up()
    al.goto(-1 * gridlength, baseY - (gridlength * 3.5))
    al.write("X")
    al.up()
    al.goto(gridlength, baseY - (gridlength * 3.5))
    al.write("O")
    al.up()
    al.goto(0, baseY - (gridlength * 3.75))

def __createButtons():
    """Creates the play again and quit buttons"""
    al.fillcolor("black")
    al.pencolor("white")
    al.up()
    al.goto(baseX - gridlength, baseY - gridlength * 5)
    for i in range(len(buttonStr)):
        __drawRectangle(buttonStr[i])
        al.up()
        al.setx(al.xcor() + gridlength * 3)
        buttonLoc.append((al.xcor(), al.ycor()))
    al.color("black")

def __drawRectangle(text):
    al.seth(0)
    al.down()
    al.begin_fill()
    for i in range(2):
        al.forward(gridlength * 2)
        al.right(90)
        al.forward(gridlength)
        al.right(90)
    al.end_fill()
    al.up()
    currX = al.xcor()
    currY = al.ycor()
    al.goto(currX + gridlength, currY - gridlength * .6)
    al.write(text, False, "center")
    al.goto(currX, currY)
    
def checkClick(x, y):
    if (x >= baseX and y >= baseY) and not gameOver:
        if (x <= baseX + (3 * gridlength)) and (y <= baseY + (3 * gridlength)):
            takeTurn(__determineBlock(x, y))
    if y >= baseY - (gridlength * 5) and y <= baseY - (gridlength * 4):
        if (x >= baseX - gridlength) and (x <= baseX + gridlength):
            al.clear()
            createBoard()
        elif (x >= baseX + (gridlength * 2)) and x <= baseX + (gridlength * 4):
            al.up()
            al.goto(0, gridlength)
            al.down()
            al.write("Thanks for playing", align="center")
            time.sleep(1)
            exit()
    
def __determineBlock(x, y):
    row = -y // gridlength
    col = x // gridlength
    return takeTurn(col, row)

def takeTurn(x, y):
    if checkSpot(x, y):
        validMove(x, y)
    else:
        return None

def checkSpot(x, y):
    return boardState[y][x] == 0

def validMove(x, y):
    if playerOneTurn:
        boardState[y][x] = 1
    else:
        boardState[y][x] = -1
    addMarker(x,y)
    if checkWin(x,y):
        turn = -1
        if playerOneTurn:
            turn = 1
        else:
            turn = 2
        __writeWinner(turn)
        gameOver = True
    elif tieChecker():
        __writeWinner(-1)
        gameOver = True
    else:
        playerOneTurn = not playerOneTurn

'''
* @param x,y: the xy coordinate pairing for the block chosen
* Check if the turn player has won. 
* @return Whether the turn player has won
'''
def checkWin(x, y):
    turn = 0
    if playerOneTurn:
        turn = 1 
    else:
        turn = -1
    horiz = __checkRow(y, turn)
    vert = __checkCol(x, turn)
    if (x == 1 and not y == 1) or (not x == 1 and y == 1):
        #Only check diagonals if the space is not on a middle edge
        diagRight = __checkDiagDown(turn)
        diagLeft = __checkDiagUp(turn)
    else:
        diagRight = False
        diagLeft = False
    return horiz or vert or diagRight or diagLeft

def __checkRow(y, turn):
    """Determines if a row is full for winning"""
    for i in range(len(boardState)):
        if boardState[y][i] != turn:
            return False
    return True

def __checkCol(x, turn):
    """Determines if a column is full for winning"""
    for i in range(len(boardState)):
        if boardState[i][x] != turn:
            return False
    return True

def __checkDiagDown(turn):
    """Determines if the downward diagonal is full for winning"""
    i = 0
    while i < len(boardState):
        if boardState[i][i] != turn:
            return False
        i += 1
    return True

def __checkDiagUp(turn):
    """Determines if the upward diagonal is full for winning"""
    i = 0
    while i < len(boardState):
        if boardState[i][len(boardState) - 1 - i] != turn:
            return False
        i += 1
    return True

def __writeWinner(turn):
    whoseTurn()
    if turn == -1:
        al.setx(0)
        al.write("It's a tie!", align = "center")
    else:
        al.write("Winner!")

def tieChecker():
    for space in boardState:
        if space == 0:
            return False
    return True

def addMarker(x, y):
    midX = (baseX + (.5 * gridlength)) + (x * gridlength)
    midY = (baseY + (.5 * gridlength)) + (y * gridlength)
    al.goto(midX,midY)
    if playerOneTurn:
        al.circle(gridlength * .5)
    else:
        al.stamp()

def whoseTurn():
    if playerOneTurn: 
        al.goto(-1 * gridlength, baseY - (gridlength * 2.75)) 
    else:
        al.goto(gridlength, baseY - (gridlength * 2.75))

createBoard()

screen.onclick(checkClick)
screen.listen()