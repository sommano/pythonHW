def find_num_digits(n):
    n_str = str(n)
    return len(n_str)

def main():
    print(find_num_digits(50))
    print(find_num_digits(20000))
    print(find_num_digits(1))

if __name__ == "__main__":
    main()
