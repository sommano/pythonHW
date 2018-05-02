from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_text = ""
    for i in text:
        encrypted_text = encrypted_text + rotate_character(i, rot)
    return encrypted_text

def main():

    text = input("Type a message:")
    rot = int(input("Rotate by:"))

    print(encrypt(text, rot))


if __name__ == "__main__":
    main()
