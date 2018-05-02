import random
import turtle

def move_random(wn, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

def are_colliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def is_in_screen(w, t):
    left_bound = - w.window_width() / 2
    right_bound = w.window_width() / 2
    top_bound = w.window_height() / 2
    bottom_bound = -w.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False
    return still_in

def main():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    wn = turtle.Screen()

    t1.shape('turtle')
    t2.shape('circle')

    left_bound = -wn.window_width() / 2
    right_bound = wn.window_width() / 2
    top_bound = wn.window_height() / 2
    bottom_bound = -wn.window_height() / 2

    t1.up()
    t1.goto(random.randrange(left_bound, right_bound),
            random.randrange(bottom_bound, top_bound))
    t1.setheading(random.randrange(0, 360))
    t1.down()

    t2.up()
    t2.goto(random.randrange(left_bound, right_bound),
            random.randrange(bottom_bound, top_bound))
    t2.setheading(random.randrange(0, 360))
    t2.down()

    while is_in_screen(wn, t1) and is_in_screen(wn, t2):
        move_random(wn, t1)
        move_random(wn, t2)

    wn.exitonclick()

if __name__ == "__main__":
    main()

