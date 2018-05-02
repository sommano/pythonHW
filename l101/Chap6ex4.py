import turtle

def fill_color(t, height):
    if height >= 200:
        return t.color("red")
    elif height < 200 and height >= 100:
        return t.color("yellow")
    else:
        return t.color("green")

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    fill_color(t, height)
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



def main():
    data = [48, -117, 200, 240, 160, 260, -220]
    max_height = max(data)
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()
