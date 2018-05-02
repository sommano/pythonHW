def analyze_text(text):
    count = 0
    e_count = 0
    for letter in text:
        if letter.isalpha() == True:
            count += 1
        if letter.lower() == 'e':
            e_count += 1

    percent = float(100*e_count/count)
    string = 'The text contains ' + str(count) + ' alphabetic characters, of which ' + str(e_count) + ' (' + str(percent) + '%) are \'e\'.'
    return string


#text = "Eeeee"
text = "Blueberries are tasteee!"
#text = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"

print(analyze_text(text))

# Don't copy these tests into Vocareum!
# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, it should pass in Vocareum. See below for more details.
#from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
#text1 = "Eeeee"
#answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
#testEqual(analyze_text(text1), answer1)

#text2 = "Blueberries are tasteee!"
#answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
#testEqual(analyze_text(text2), answer2)

#text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
#answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
#testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
#text4 = "Eeeee"
#answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
#testEqual(analyze_text(text4), answer4)

#text5 = "Blueberries are tasteee!"
#answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
#testEqual(analyze_text(text5), answer5)

#text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
#answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
#testEqual(analyze_text(text6), answer6)