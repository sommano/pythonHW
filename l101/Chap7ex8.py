def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + '#'

    return line_str

def stairs(n):
    stair_str = ''
    for level_len in range(n):
        stair_str += (line(level_len+1) + '\n')

    return stair_str

def main():
    print(stairs(5))

if __name__ == "__main__":
    main()

