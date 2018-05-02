my_list = [76, 92.3, 'hello', True, 4, 76]

my_list.append("apple")         # a
my_list.append(76)              # a
my_list.insert(3, "cat")        # b
my_list.insert(0, 99)           # c

print(my_list.index("hello"))   # d
print(my_list.count(76))        # e
my_list.remove(76)              # f
my_list.pop(my_list.index(True)) # g

print (my_list)
