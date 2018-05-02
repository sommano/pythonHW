from helpers import alphabet_position, rotate_character

def encrypt(text, encryption_keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ""
    key = ""
    count = 0

    for letter in text:
        if letter.lower() in alphabet:
            key = key + encryption_keyword[count].lower()
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
    #text = input("Type a message:")
    #encryption_keyword = input("Encryption key:")

    #text = "The crow flies at midnight!"
    #encryption_keyword = "boom"

    text = "Sailing <3 ships thru br0ken harbors"
    encryption_keyword = "NeilYoung"
    print(encrypt(text, encryption_keyword))
    print("Feqwgba <3 fnvta effo ox0xiv syfvbxf")
if __name__ == "__main__":
    main()


#text = "Sailing <3 ships thru br0ken harbors"
#encryption_keyword = "NeilYoung"
#print("Sailing <3 ships thru br0ken harbors")
#print("Feqwgba <3 fnvta effo ox0xiv syfvbxf")

#text = "BaRFoo"
#encryption_keyword = "BaZ"
#print("BaRFoo")
#print("CaQGon")