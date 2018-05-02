# TODO: use def to define a function called area_of_circle which takes an argument called r

    # TODO implement your function to return the area of a circle whose radius is r
import math
def area_of_circle(r):
    return math.pi*r**2

print(area_of_circle(0))

# Below are some tests which can give you an indication that your code seems to be correct.

# IMPORTANT: You should NOT include this part when you submit in Vocareum.
# When you submit, only include the function above.
#from test import testEqual

#t = area_of_circle(0)
#testEqual(t, 0)
#t = area_of_circle(1)
#testEqual(t,math.pi)
#t = area_of_circle(100)
#testEqual(t, 31415.926535897932)
#t = area_of_circle(-1)
#testEqual(t, math.pi)
#t = area_of_circle(-5)
#testEqual(t, 25 * math.pi)
#t = area_of_circle(2.3)
#testEqual(t, 16.61902513749)