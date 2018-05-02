# Sorts a list using bubble sort.
def bubble_sort(list):
    is_sorted = False
    while not is_sorted:
        num_swaps = 0 ## Number of swaps made
        for i in range(len(list)-1):
            if list[i+1] < list[i]:
                #list[i], list[i + 1] = list[i + 1], list[i]
                temporary = list[i]
                list[i] = list[i+1]
                list[i+1] = temporary
                num_swaps = num_swaps + 1
        if num_swaps == 0:
            is_sorted = True
    return list

print(bubble_sort([5, 4, 3, 2, 1]))
#from test import testEqual
#testEqual(bubble_sort([0]), [0])  # Sorts a single element, returns same list
#testEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Sorted list is the same
#testEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
#testEqual(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
