def sum_to(n):
    result = (n * (n + 1)) / 2
    return result

def main():
    # Now lets see how well this works
    t = sum_to(0)
    print("The sum from 1 to 0 is",t)
    t = sum_to(10)
    print("The sum from 1 to 10 is",t)
    t = sum_to(5)
    print("The sum from 1 to 5 is",t)

if __name__ == "__main__":
    main()
