# draw an equilateral triangle
import turtle

wn = turtle.Screen()
eqi = turtle.Turtle()
eqi.color("blue")
for i in range(3):
    eqi.forward(100)
    eqi.left(360/3)


# draw a square
import turtle

wn = turtle.Screen()
square = turtle.Turtle()
square.color("red")
for i in range(4):
    square.forward(100)
    square.left(360/4)


# draw a hexagon
import turtle

wn = turtle.Screen()
hexa = turtle.Turtle()
hexa.color("purple")
for i in range(6):
    hexa.forward(100)
    hexa.left(360/6)


# draw an octogon
import turtle

wn = turtle.Screen()
octo = turtle.Turtle()
octo.color("green")
for i in range(8):
    octo.forward(75)
    octo.left(360/8)
wn.exitonclick()