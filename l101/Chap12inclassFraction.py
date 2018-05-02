
class Fraction:
    def __init__(self, numerator = 0, denominator = 0):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        a = "Numerator = " + str(self.numerator) + " Denominator = " + str(self.denominator)
        return a

    def add(self,other_numerator,other_denominator):
        new_numerator = self.numerator + other_numerator
        new_denominator = self.denominator + other_denominator
        return new_numerator / new_denominator

    def multiply(self,other_numerator,other_denominator):
        new_numerator = self.numerator * other_numerator
        new_denominator = self.denominator * other_denominator
        return new_numerator / new_denominator

    def reciprocal(self):

        return self.denominator / self.numerator

    def simplify(self):
        return  self.numerator / self.denominator


a = Fraction(2,8)
print(a)
print(a.add(1,4))

print(a.multiply(1,4))
print(a.reciprocal())

print(a.simplify())

