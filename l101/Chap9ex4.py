#from test import testEqual

def reverse(text):
    new_string = text[::-1]
    return new_string

print(reverse("happy"))
#testEqual(reverse("happy"), "yppah")
#testEqual(reverse("Python"), "nohtyP")
#testEqual(reverse(""), "")
