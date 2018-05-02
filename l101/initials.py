def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    #Ozzie Smith OS
    #Bonnie blair BB
    #George G
    #Daniel Day Lewis DDL
    #xs = (fullname)
    initial = ""
    split_name = fullname.split()
    print(split_name)
    for i in split_name:
        initial = initial + i[0].upper()
    return initial

def main():
    # some more code here (input and print statements)
    fullname = input("What is your full name?")
    #fullname = "Daniel Day Lewis"
    initials = get_initials(fullname)
    print("What is you full name?:",fullname)
    print("Your initials are,",initials)

if __name__ == '__main__':
    main()