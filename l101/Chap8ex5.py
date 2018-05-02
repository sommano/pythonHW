import sys

def workout_coach(lift_name, wt):
    print("Time to", lift_name, wt, "pounds! You got this!")

def main():
    lifts = ["squat", "bench", "deadlift"]
    for lift in lifts:
        keep_lifting = "yes"
        weight = 0
        input_prompt = "Keep doing the " + lift + "? Enter yes for the next set."
        while keep_lifting == "yes":
            weight = weight + 10
            if lift == "bench" and weight > 200:
                break
            else:
                workout_coach(lift, weight)
            keep_lifting = input(input_prompt)

if __name__ == "__main__":
    main()

