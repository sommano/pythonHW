# TODO: add the Car class
class Car:
    def __init__(self, amount):
        self.gas_level = amount

    def add_gas(self, amount):
        self.gas_level += amount

    def fill_up(self):
        if self.gas_level > 13.0:
            return 0.0
        else:
            tank = 13.0 - self.gas_level
            return tank

def main():
    c = Car(9)
    print(c.fill_up())

if __name__ == "__main__":
    main()


# some tests to check your code, Do Not Post These in Vocareum
#from test import testEqual
#testEqual( Car(10).fill_up(), 3 )
#testEqual( Car(20).fill_up(), 0 )
#testEqual( Car(5.5).fill_up(), 7.5 )
#testEqual( Car(12.5).fill_up(), 0.5 )
#testEqual( Car(13).fill_up(), 0 )
