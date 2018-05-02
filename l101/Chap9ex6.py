def mirror(text):
    front = text
    back = reverse(text)
    mirror_string = front+back
    return mirror_string

def reverse(text):
    new_string = text[::-1]
    return new_string

print(mirror("good"))

#from test import testEqual
#testEqual(mirror('good'), 'gooddoog')
#testEqual(mirror('Python'), 'PythonnohtyP')
#testEqual(mirror(''), '')
#testEqual(mirror('a'), 'aa')
