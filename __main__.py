from turtle import Turtle, Screen
import time

baseX = -75
baseY = -75
gridlength = 50
boardState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    """Establish the backend and frontend boards"""
    global boardState
    global playerOneTurn
    global gameOver
    boardState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    playerOneTurn = True
    gameOver = False
    for x in range(3):
        for y in range(3):
            __createBox(x, y)
    __createLabels()
    __createButtons()
    whoseTurn()


def __createBox(col, row):
    """Creating a box at (col, row) location"""
    x = baseX + (col * 50)
    y = baseY + (row * 50)
    al.up()
    al.goto(x, y)
    al.down()
    al.seth(90)
    for _ in range(4):
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
    """Draw a rectangle with 'text' inside"""
    al.seth(0)
    al.down()
    al.begin_fill()
    for _ in range(2):
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
    """Determine whether the click is inside the board"""
    print(f"Click registered at {x}, {y}")
    if not gameOver and ((x >= baseX and x <= baseX + (3 * gridlength)) and
                         (y >= baseY and y <= baseY + (3 * gridlength))):
        block = __determineBlock(x, y)
        takeTurn(block[0], block[1])
    elif y >= baseY - (gridlength * 6) and y <= baseY - (gridlength * 5) and (
         (x >= baseX - gridlength) and (x <= baseX + gridlength)):
        al.clear()
        createBoard()
    elif (x >= baseX + (gridlength * 2)) and x <= baseX + (gridlength * 4):
        al.up()
        al.goto(0, gridlength * 3)
        al.down()
        al.write("Thanks for playing", align="center")
        al.up()
        al.sety(al.ycor() - gridlength // 4)
        time.sleep(1)
        exit()


def __determineBlock(x, y):
    """Find out which block was clicked at (x,y) position"""
    row = -1
    col = -1
    for i in range(len(boardState)):
        if y >= (baseY
                 + (i * gridlength)) and y <= baseY + ((i + 1) * gridlength):
            row = i
            break
    for j in range(len(boardState[0])):
        if x >= (baseX
                 + (j * gridlength)) and x <= baseX + ((j + 1) * gridlength):
            col = j
            break

    print("Col: {c}, Row: {r}".format(c=col, r=row))
    return (int(col), int(row))


def takeTurn(x, y):
    """Current player takes their turn if the click is valid"""
    if checkSpot(x, y):
        validMove(x, y)
    else:
        return None


def checkSpot(x, y):
    """Determine if the square has been moved in"""
    return boardState[y][x] == 0


def validMove(x, y):
    """Make a move on the expected square"""
    global gameOver
    global playerOneTurn
    if playerOneTurn:
        boardState[y][x] = 1
    else:
        boardState[y][x] = -1
    addMarker(x, y)
    if checkWin(x, y):
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
    print(boardState)
    whoseTurn()


def checkWin(x, y):
    """Check if the turn player has won"""
    turn = 0
    if playerOneTurn:
        turn = 1
    else:
        turn = -1
    horiz = __checkRow(y, turn)
    vert = __checkCol(x, turn)
    if not((x == 1 and y != 1) or (x != 1 and y == 1)):
        # Only check diagonals if the space is not on a middle edge
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


def __checkDiagUp(turn):
    """Determines if the upward diagonal is full for winning"""
    i = 0
    while i < len(boardState):
        if boardState[i][i] != turn:
            return False
        i += 1
    return True


def __checkDiagDown(turn):
    """Determines if the downward diagonal is full for winning"""
    i = 0
    while i < len(boardState):
        if boardState[i][(len(boardState) - 1) - i] != turn:
            return False
        i += 1
    return True


def __writeWinner(turn):
    """The turtle writes who won or tied"""
    whoseTurn()
    if turn == -1:
        al.setx(0)
        al.write("It's a tie!", align="center")
    else:
        al.sety(al.ycor() + gridlength / 3)
        al.write("Winner!", align="center")


def tieChecker():
    """Check if all squares have been filled"""
    for y in range(len(boardState)):
        for x in range(len(boardState[0])):
            if boardState[y][x] == 0:
                return False
    return True


def addMarker(x, y):
    """Visually put a marker on the moved-to square"""
    midX = (baseX + (.5 * gridlength)) + (x * gridlength)
    locY = (baseY + (y * gridlength))
    al.up()
    al.goto(midX, locY)
    if playerOneTurn:
        al.down()
        al.circle(gridlength * .5)
    else:
        al.sety(al.ycor() + (gridlength * .5))
        al.down()
        al.stamp()
    al.up()


def whoseTurn():
    """Move the turtle to the correct side in the turn marker"""
    if playerOneTurn:
        al.goto(-1 * gridlength, baseY - (gridlength * 2.75))
    else:
        al.goto(gridlength, baseY - (gridlength * 2.75))


createBoard()

screen.onclick(checkClick)
screen.mainloop()
