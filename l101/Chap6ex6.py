#from test import testEqual

def is_odd(n):
    if n % 2 != 0:
        return False
    else:
        return True

num = [10, 5, 1, 0]

for x in num:
    is_odd(x)

#testEqual(is_odd(10), False)
#testEqual(is_odd(5), True)
#testEqual(is_odd(1), True)
#testEqual(is_odd(0), False)