def test(scores):
    sum = 0
    for i in scores:
        sum = sum + i
    average = sum / max(len(scores),1)
    if average >= 70 and min(scores) > 50:
        return "Pass"
    elif average <70 or min(scores) <50:
        return "fail"

scores = [100, 75, 45]
print(test(scores))

