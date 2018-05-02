def space_line(spaces, hashes):
    return spaces * ' ' + hashes * '#'

def triangle(n):
    triangle_str = ''
    for i in range(n):
        triangle_str += (space_line(n-i-1, 2*i+1) + '\n')
    return triangle_str

def diamond(n):
    diamond_str = triangle(n)
    for i in range(n-2, -1, -1):
        diamond_str += (space_line(n-i-1, 2*i+1) + '\n')
    return diamond_str

def main():
    print(diamond(7))

if __name__ == "__main__":
    main()

