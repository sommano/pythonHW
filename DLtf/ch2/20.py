import itertools
class Recursion3Term:
 def __init__(self, a0, a1, u0, u1):
self.coeff = [a1, a0]
self.initial = [u1, u0]
 def __iter__(self):
u1, u0 = self.initial
yield u0 # (see also Iterators section in Chapter 9)
yield u1
a1, a0 = self.coeff
while True :
u1, u0 = a1 * u1 + a0 * u0, u1
yield u1
 def __getitem__(self, k):
return list(itertools.islice(self, k, k + 1))[0]
