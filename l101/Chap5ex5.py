import turtle

def draw_poly(t, sides, side_length):
    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)

def main():
    wn = turtle.Screen()       # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color('hotpink')
    tess.pensize(3)

    draw_poly(tess, 3, 50)

if __name__ == "__main__":
    main()
