import turtle

def draw_star(t, n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)

def main():
    sam = turtle.Turtle()
    draw_star(sam, 7)

if __name__ == "__main__":
    main()
