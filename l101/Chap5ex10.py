import turtle

def draw_sprite(t, legs, leg_length):
    angle = 360/legs
    for i in range(legs):
        t.forward(leg_length)
        t.backward(leg_length)
        t.left(angle)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    draw_sprite(alex, 15, 120)

    wn.exitonclick()

if __name__ == "__main__":
    main()
