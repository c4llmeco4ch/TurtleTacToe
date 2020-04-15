from turtle import Turtle

'''
* For students who will be learning
* to make Tic-Tac-Toe with turtle,
* this is a brief introduction into
* how we can make the board itself.

* Step 1: Make a square
* Step 2: Make a row
* Step 3: Make 3 rows using goto
'''
al = Turtle()
al.shape("square")
squareLength = 50
for k in range(3):
    for i in range(3):
        for j in range(4):
            al.fd(squareLength)
            al.right(90)
        al.right(90)
        al.fd(squareLength)
        al.left(90)
    al.up()
    al.goto((k + 1) * -1 * squareLength, 0)
    al.down()
