def is_leap(year):
    year = int(year)
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = input("Enter year:")

print(is_leap(year))