def sum_to(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

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
