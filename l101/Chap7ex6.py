def line(n):
    hash = ""
    for x in range(n):
        hash = hash + "#"
    return hash


def square(n):
    for x in range(n):
        print(line(n))


square(5)