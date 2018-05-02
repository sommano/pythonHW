#Write a function that takes in an integer and then displays the multiplication table of that size.
# For example, if the given integer was 3, the following multiplication table would be displayed:
def multi_table(number):
    table = ""
    for i in range(number+1):
        for j in range(number+1):
            table = str((number-i)*(number-j)) + "    " + table
        table = "\n" + table


    return table

print(multi_table(int(input("Enter a multiplication table size:"))))