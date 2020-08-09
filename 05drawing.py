#Sara Margaret Rizzo
#2020-08-08
#This program draws three flowers and some grass

import turtle
wn = turtle.Screen()

#flower1
turtle.color("green")
turtle.shape("square")
#turtle.forward(5)
#turtle.left(90)
turtle.pensize(5)
turtle.pendown()
turtle.right(90)
turtle.forward(-100)
turtle.right(90)

turtle.color("brown")
turtle.pendown()
turtle.begin_fill()
for size in range(10):
    turtle.forward(20)
    turtle.right(36)
turtle.end_fill()

turtle.shape("circle")
turtle.penup()
turtle.color("yellow")

for size in range(10):
    turtle.forward(20)
    turtle.stamp()
    turtle.right(36)

#flower2
turtle.penup()
turtle.goto(0,0)
turtle.forward(100)
turtle.color("green")
turtle.shape("square")
turtle.pensize(5)
turtle.pendown()
turtle.left(90)
turtle.forward(-100)
turtle.right(90)

turtle.color("brown")
turtle.pendown()
turtle.begin_fill()
for size in range(10):
    turtle.forward(20)
    turtle.right(36)
turtle.end_fill()

turtle.shape("circle")
turtle.penup()
turtle.color("MediumPurple")

for size in range(10):
    turtle.forward(20)
    turtle.stamp()
    turtle.right(36)

#flower3
turtle.penup()
turtle.goto(0,0)
turtle.backward(100)    
turtle.color("green")
turtle.shape("square")
#turtle.forward(5)
turtle.right(90)
turtle.pensize(5)
turtle.pendown()
#turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.color("brown")
turtle.pendown()
turtle.begin_fill()
for size in range(10):
    turtle.forward(20)
    turtle.right(36)
turtle.end_fill()

turtle.shape("circle")
turtle.penup()
turtle.color("Magenta")

for size in range(10):
    turtle.forward(20)
    turtle.stamp()
    turtle.right(36)
    
#grass
turtle.penup()
turtle.goto(-200,0)
turtle.right(180)
turtle.shape("circle")
turtle.pensize(3)
turtle.color("PaleGreen")

for size in range(40):
    turtle.forward(10)
    turtle.stamp()

wn.exitonclick()  