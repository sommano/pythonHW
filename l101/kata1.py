def correct(string):
    answer = ""
    for character in string:
        if character == "5":
            answer = answer + "S"        
        elif character == "0":
            answer = answer + "O"
        elif character == "1":
            answer = answer + "I"
        elif character not in "501":
            answer = answer + character

    return answer