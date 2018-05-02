#from test import testEqual

def is_even(n):
    if n % 2 == 0:
        print("For number",n,"True")
        return True
    else:
        print("For number", n, "False")
        return False

num = [10, 5, 1, 0]

for x in num:
    is_even(x)


#testEqual(is_even(10), True)
#testEqual(is_even(5), False)
#testEqual(is_even(1), False)
#testEqual(is_even(0), True)
