import turtle

def draw_sprite(t, legs, leg_length):
    angle = 360/legs
    for i in range(legs):
        t.forward(leg_length)
        t.backward(leg_length)
        t.left(angle)

def fancy_square(t, sz, lgs, lgl):
    for i in range(4):
        t.forward(sz)
        draw_sprite(t, lgs, lgl)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    fancy_square(alex, 100, 10, 15)

    wn.exitonclick()

if __name__ == "__main__":
    main()
