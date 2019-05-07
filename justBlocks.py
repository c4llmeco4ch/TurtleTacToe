from turtle import *


al = Turtle()
al.shape("square")
squareLength = 50
for i in range(3):
    for j in range(4):
        al.fd(squareLength)
        al.right(90)
    al.right(90)
    al.fd(squareLength)
    al.left(90)