import math

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

    def distance_from_point(self, otherP):
        dx = (otherP.get_x() - self.x)
        dy = (otherP.get_y() - self.y)
        return math.sqrt(dy**2 + dx**2)

def main():
    p = Point(3, 3)
    q = Point(6, 7)
    print(p.distance_from_point(q))

if __name__ == "__main__":
    main()
