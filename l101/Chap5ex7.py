import turtle

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

def main():
    wolfram = turtle.Turtle()
    draw_star(wolfram)

if __name__ == "__main__":
    main()
