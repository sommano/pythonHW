class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

def main():
    p = Point(7, 6)
    print(p)
    p.move(5, 10)
    print(p)

if __name__ == "__main__":
    main()
