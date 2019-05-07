from turtle import *
import time

baseX = -75
baseY = -75
gridlength = 50
boardState = [[0,0,0],[0,0,0],[0,0,0]]
buttonStr = ["Play Again", "Exit"]
buttonLoc = []
al = Turtle()
al.shape("turtle")
al.speed(7)
playerOneTurn = True
gameOver = False
errorText = ""

def createBoard():
    for x in range (3):
        for y in range (3):
            __createBox(x, y)
    __createLabels()
    __createButtons()
    whoseTurn()

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
    al.goto(0, baseY - (gridlength * 4.25))

def __createButtons():
    al.fillcolor("black")
    al.pencolor("white")
    al.up()
    al.goto(baseX - gridlength, baseY - gridlength * 5)
    for i in range(len(buttonStr)):
        drawRectangle(buttonStr[i])
        al.up()
        al.setx(al.xcor() + gridlength * 3)
        buttonLoc.append((al.xcor(), al.ycor()))
    al.color("black")

def drawRectangle(text):
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
    
    
def takeTurn(block):
    if checkSpot(block):
        __validMove(block)
    else:
        return None

def __validMove(block):
    x = (block % 3) - 1
    y = (block - 1) // 3
    if playerOneTurn:
        boardState[y][x] = 1
    else:
        boardState[y][x] = -1
    __addMarker(x,y)
    #TODO: Add checkWin()
    #Else, switch players

def __addMarker(x, y):
    midX = (baseX + (.5 * gridlength)) + (x * gridlength)
    midY = (baseY + (.5 * gridlength)) + (y * gridlength)
    al.goto(midX,midY)
    if playerOneTurn:
        al.circle(gridlength * .5)
    else:
        al.stamp()

def checkSpot(block):
    x = (block % 3) - 1
    y = (block - 1) // 3
    return boardState[y][x] == 0

def whoseTurn():
    if playerOneTurn: 
        al.goto(-1 * gridlength, baseY - (gridlength * 4.5)) 
    else:
        al.goto(gridlength, baseY - (gridlength * 4.5))

createBoard()
time.sleep(10)



