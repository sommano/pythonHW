def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + '#'

    return line_str

def rectangle(width, height):
    rectangle_str = ''
    for i in range(height):
        rectangle_str += (line(width) + '\n')

    return rectangle_str

def main():
    print(rectangle(5, 3))

if __name__ == "__main__":
    main()

