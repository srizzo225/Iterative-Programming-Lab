#Sara Margaret Rizzo
#2020-08-08
#This program creates a polygon



#Sara Margaret Rizzo
#2020-08-08
#This program creates a polygon

import turtle

wn = turtle.Screen()

#ask the user for the number of sides 
sides = int(input("How many sides should the polygon have? "))
#the length of the side
length = int(input("How long should each side be? "))
#the color of the line
tcol = input("What color should the lines be? ")
#the fill color of a regular polygon
fillcol = input("What color should the polygon be? ")

# draw the polygon
tess = turtle.Turtle()
tess.color(tcol)
tess.fillcolor(fillcol)

angle = 360 / sides

tess.begin_fill()
for count in range(sides):
  tess.forward(length)
  tess.left(angle)

#close the polygon and fill it in
tess.end_fill()

wn.exitonclick()  