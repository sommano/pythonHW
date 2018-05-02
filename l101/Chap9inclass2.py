def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """
    # TODO: Fill in details
    for i in range(len(string) - 1):
        if string[i] > string[i + 1]:
            return False

    return True


print(is_sorted("ABC"))

#is_sorted("ABC") == True
#is_sorted("aBc") == False
#is_sorted("dog") == False