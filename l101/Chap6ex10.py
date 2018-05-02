from test import testEqual

def is_rightangled(a, b, c):
    rightangled = False

    if a > b and a > c:
        rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return rightangled

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)
