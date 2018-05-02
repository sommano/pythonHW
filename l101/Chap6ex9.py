

#from test import testEqual

def is_rightangled(a, b, c):
    sides = [a, b, c]
    sides = sorted(sides)
    hyp = sides[2]
    side1 = sides[0]
    side2 = sides[1]

    if round(hyp**2, 3) == round((side1**2 + side2**2),3):
        return True
    else:
        return False

#a = float(input("Enter length of side A:"))
#b = float(input("Enter length of side B:"))
#c = float(input("Enter length of side C:"))
a = 4.1
b = 8.2
c = 9.16787
print(is_rightangled(a,b,c))


#testEqual(is_rightangled(1.5, 2.0, 2.5), True)
#testEqual(is_rightangled(4.0, 8.0, 16.0), False)
#testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
#testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
#testEqual(is_rightangled(4.1, 8.2, 9.168), False)
#testEqual(is_rightangled(0.5, 0.4, 0.64031), True)

