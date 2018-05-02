#from test import testEqual

def reverse(text):
    new_string = text[::-1]
    return new_string



def is_palindrome(text):
    regular_string = text
    reverse_string = reverse(text)
    if regular_string == reverse_string:
        return True
    else:
        return False



#testEqual(is_palindrome('abba'), True)
#testEqual(is_palindrome('abab'), False)
#testEqual(is_palindrome('straw warts'), True)
#testEqual(is_palindrome('a'), True)
#testEqual(is_palindrome(''), True)


print(is_palindrome("abba"))