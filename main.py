from turtle import *
import time

baseX = -75
baseY = -75
gridlength = 50
boardState = [[0,0,0],[0,0,0],[0,0,0]]
al = Turtle()
al.shape("turtle")
al.speed(7)
playerOneTurn = True
gameOver = False

def createBoard():
    for x in range (3):
        for y in range (3):
            __createBox(x, y)
    __createLabels()

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
    al.goto(x + (gridlength / 2), y + (gridlength / 2))
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
    


def checkSpot(block):
    x = (block % 3) - 1
    y = (block - 1) // 3
    return boardState[y][x] == 0

createBoard()
time.sleep(5)

