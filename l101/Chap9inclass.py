from test import testEqual

def remove_char(string, char):

    new_str = ''

    for index in range(len(string)):
        if string[index] != char:
            new_str = new_str + string[index]

    return new_str

testEqual(remove_char('aardvark', 'a'), 'rdvrk')
testEqual(remove_char('aardvark', 'k'), 'aardvar')
testEqual(remove_char('asdf', 'z'), 'asdf')
testEqual(remove_char('', 'a'), '')
