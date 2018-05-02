from test import testEqual

def remove(occurrence,string):
    index = string.find(occurrence)
    if index < 0: # substr doesn't exist in original_string
        return string
    return_str = string[:index] + string[index+len(occurrence):]
    return return_str

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
