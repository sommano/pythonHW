def pick_activity(temp, damp):
    if temp == "hot" and damp == "wet":
        message = "Watch Netflix"
    elif temp == "hot" and damp == "dry":
        message = "Go swimming"
    elif temp == "cold" and damp == "wet":
        message = "Paint!"
    elif temp == "cold" and damp == "dry":
        message = "Got to a cafe and read"
    else:
        message = "Invalid input. Enter hot or cold, wet or dry."
    return message

def main():
    temp = input("Is the weather hot or cold?")
    damp = input("Is the humidity wet or dry?")
    print(pick_activity(temp, damp))

if __name__ == "__main__":
    main()
