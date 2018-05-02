from test import testEqual

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


r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.contains(Point(0, 0)), True)
testEqual(r.contains(Point(3, 3)), True)
testEqual(r.contains(Point(3, 7)), False)
testEqual(r.contains(Point(3, 5)), False)
testEqual(r.contains(Point(3, 4.99999)), True)
testEqual(r.contains(Point(-3, -3)), False)
