def pos_or_neg(num):
    if num > 0:
        print('positive')
    elif num < 0:
        print('negative')


def print_positives(the_ints):
    for num in the_ints:
        if num > 0:
            print(num)


def print_signed_integers(the_ints, the_sign):
    if the_sign == 'positive':
        for i in the_ints:
            if i > 0:
                print(i)
    elif the_sign == 'negative':
        for i in the_ints:
            if i < 0:
                print(i)

