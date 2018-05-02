import turtle

def draw_square(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("blue")

    alex = turtle.Turtle()
    alex.color('green')
    alex.pensize(3)

    for i in range(6):
        draw_square(alex, 20*i)
        alex.penup()
        alex.goto(-10 * i, -10*i)
        alex.pendown()

    wn.exitonclick()

if __name__ == "__main__":
    main()
