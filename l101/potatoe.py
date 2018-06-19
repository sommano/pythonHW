def solve(s):
    upper=0
    lower=0
    answer=""
    for letter in s:
        if letter.islower() == True:
            lower = lower + 1
        elif letter.isupper() == True:
            upper = upper + 1      
    if lower == upper:
        return s.lower()
    elif upper > lower:
        return s.upper()
    elif lower > upper:
        return s.lower()