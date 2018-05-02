from helpers import alphabet_position, rotate_character

def encrypt(text, encryption_keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ""
    key = ""
    count = 0

    for letter in text:
        if letter.lower() in alphabet:
            key = key + encryption_keyword[count]
            count = count +1
            if count > len(encryption_keyword)-1:
                count = 0
        elif letter.lower() not in alphabet:
            key = key + letter

    for i in range(len(key)):
        if key[i] in alphabet:
            rot = alphabet_position(key[i])
            encrypted_text = encrypted_text + rotate_character(text[i],rot)
        elif key[i] not in alphabet:
            encrypted_text = encrypted_text + key[i]

    #print(key)
    return encrypted_text

def main():
    text = input("Type a message:")
    encryption_keyword = input("Encryption key:")
    #text = "The crow flies at midnight!"
    #encryption_keyword = "boom"
    print(encrypt(text, encryption_keyword))
    #print("Uvs osck rmwse bh auebwsih!")
    #print(text)
if __name__ == "__main__":
    main()