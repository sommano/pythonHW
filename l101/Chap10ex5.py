import random

def max(alist):
    max = 0
    for e in alist:
        if e > max:
            max = e
    return max

alist = []
for i in range(100):
    alist.append(random.randint(0, 1000))

print(max(alist))
