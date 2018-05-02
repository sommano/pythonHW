import turtle


def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        for x in range(4):
            t.forward(sz)
            t.left(90)
        t.left(90)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("blue")
    alex.speed(30)
    for i in range(6):
        draw_square(alex, 100)
        alex.goto(0, 0)
        alex.right(15)
    wn.exitonclick()


if __name__ == "__main__":
    main()