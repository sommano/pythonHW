def sort_contacts(dictionary):

    asort = sorted(dictionary.items())
    #print(asort)
    #print(len(asort))
    b = []
    for i in range(len(asort)):
        b.append((asort[i][0],asort[i][1][0],asort[i][1][1]))
    return b

dictionary = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
     "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
     "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}



# The code below is just for your testing purposes. Make sure you pass all the tests.
# In Vocareum, only put code for the sort_contacts function above
#from test import testEqual


def main():
    print(sort_contacts(dictionary))

if __name__ == "__main__":
    main()