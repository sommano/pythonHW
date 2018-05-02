import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')
lance.penup()
andy.penup()

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)
lance.pendown()
andy.pendown()
# your code goes here

for distance in range(0,22,1): # generates [0..22]

    andy_distance = random.randrange(0,22)
    lance_distance = random.randrange(0,22)
    # move each turtle forward by distance
    andy.forward(andy_distance)
    lance.forward(lance_distance)

print(andy.distance(-100,20))
print(lance.distance(-100,-20))
wn.exitonclick()