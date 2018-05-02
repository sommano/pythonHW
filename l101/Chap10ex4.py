import random

def count_odd(alist):
    odd = 0
    for e in alist:
        if e % 2 != 0:
            odd = odd + 1
    return odd

def main():
    # make a random list to test the function
    alist = []
    for i in range(100):
        alist.append(random.randint(0, 1000))

    print(count_odd(alist))

if __name__ == "__main__":
    main()
