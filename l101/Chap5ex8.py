import turtle

def draw_star(wolfram):
    for i in range(5):
        wolfram.forward(100)
        wolfram.left(216)

def draw_multi_stars(wolfram, n):
    for i in range(n):
        draw_star(wolfram)
        wolfram.penup()
        wolfram.forward(350)
        wolfram.right(144)
        wolfram.pendown()

def main():
    wolfram = turtle.Turtle()
    wolfram.speed(20)
    wolfram.penup()
    wolfram.goto(-170,30)
    wolfram.pendown()

    draw_multi_stars(wolfram, 5)



if __name__ == "__main__":
    main()


