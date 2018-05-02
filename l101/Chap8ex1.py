

def print_triangular_numbers(n):
    tri = ""
    for i in range(1, n+1):
        i = (i*(i+1)) / 2
        i = int(i)
        tri = tri + str(i) + "\n"

    return tri

number = input("Input a number for triangular?:")
print(print_triangular_numbers(int(number)))


