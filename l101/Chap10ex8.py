def count_words(listt):
    count = 0
    for i in listt:
        if type(i) == str:
            length = len(i)
            if length == 5:
                count = count +1
    return count

listt = ["words", "words", "run", "happy", "one", 3, 4, 5]
print(count_words(listt))
