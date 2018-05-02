class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def __str__(self):
        a = "Rectangle width=" + str(self.width) + "height=" + str(self.height)
        return a

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return self.width + self.width + self.height + self.height

    def square(self):
        if self.width != 0 or self.height != 0:
            if self.width == self.height:
                return "This rectangle is a Sqaure"
            else:
                return "This rectangle is a rectangle"

    #def comparison(self):


r = Rectangle(5,4)
s = Rectangle(2,2)

print(r)
print(s)

print("Area of r is:",r.area())
print("Area of s is:",s.area())

print("Perimeter of r:",r.perimeter())
print("Perimeter of s:", r.square())


