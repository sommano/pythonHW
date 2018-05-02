def sum_of_squares(xs):
    sums = 0
    for i in xs:
        sums = sums + i**2
    return sums

xs = [2,3,4]
print(sum_of_squares(xs))
