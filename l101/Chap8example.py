def course_grader(test_scores):
    total = 0

    for i in range(len(test_scores)):
        total = total + test_scores[i]

    average = total / max(len(test_scores),1)

    if average >= 70 and min(test_scores) >= 50:
        grade = "pass"
    elif average < 70:
        grade = "fail"
    elif min(test_scores) < 50:
        grade = "fail"
    return grade


def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
