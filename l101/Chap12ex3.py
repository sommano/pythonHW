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

    # TODO define a method called slope_from_origin here


# some tests to check your code
from test import testEqual
testEqual( Point(4, 10).slope_from_origin(), 2.5 )
testEqual( Point(5, 10).slope_from_origin(), 2 )
testEqual( Point(0, 10).slope_from_origin(), None )
testEqual( Point(20, 10).slope_from_origin(), 0.5 )
testEqual( Point(20, 20).slope_from_origin(), 1 )
testEqual( Point(4, -10).slope_from_origin(), -2.5 )
testEqual( Point(-4, -10).slope_from_origin(), 2.5 )
testEqual( Point(-6, 0).slope_from_origin(), 0 )
