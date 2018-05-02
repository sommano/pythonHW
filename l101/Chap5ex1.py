import turtle

def draw_square(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color('hotpink')
    alex.pensize(3)

    for i in range(5):
        draw_square(alex, 20)
        alex.penup()
        alex.forward(40)
        alex.pendown()

    wn.exitonclick()

if __name__ == "__main__":
    main()
