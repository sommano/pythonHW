def fibonacci(n):
    a = 1
    b = 1
    string = [a, b]
    for i in range(n-1):
        a, b = b, a + b

        string.append(b)
        print(string)
    return a
3
print(fibonacci(3))

