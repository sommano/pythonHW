def count(obj, alist):
    count = 0
    for e in alist:
        if e == obj:
            count = count + 1
    return count

def is_in(obj, alist):  # cannot be called in() because in is a reserved keyword
    for e in alist:
        if e == obj:
            return True
    return False

def reverse(alist):
    reversed = []
    for i in range(len(alist)-1, -1, -1): # step through the original list backwards
        reversed.append(alist[i])
    return reversed

def index(obj, alist):
    for i in range(len(alist)):
        if alist[i] == obj:
            return i
    return -1

def insert(obj, index, alist):
    new_list = []
    for i in range(len(alist)):
        if i == index:
            new_list.append(obj)
        new_list.append(alist[i])
    return new_list

def main():
    alist = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
    print(count(1, alist))
    print(is_in(4, alist))
    print(reverse(alist))
    print(index(2, alist))
    print(insert('cat', 4, alist))

if __name__ == "__main__":
    main()
