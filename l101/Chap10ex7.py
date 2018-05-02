import random

def sum_negative(alist):
    sum = 0
    for e in alist:
        if e < 0:
            sum = sum + e
    return sum

alist = []
for i in range(100):
    alist.append(random.randrange(-1000, 1000))

print(sum_negative(alist))
