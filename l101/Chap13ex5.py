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


class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, init_p, init_w, init_h):

        self.location = init_p
        self.width = init_w
        self.height = init_h

    def __repr__(self):
        return "I'm a rectangle with width {} and height {}".format(self.width, self.height)

    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp

r = Rectangle(Point(100, 50), 10, 5)
testEqual(r.width, 10)
testEqual(r.height, 5)
r.transpose()
testEqual(r.width, 5)
testEqual(r.height, 10)
