def substitution_cipher(message, cipher):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc  = list(abc)
    encrypted = ''

    for letter in message:
        if letter == ' ':
            encrypted = encrypted + ' '
        else:
            pos = abc.index(letter)
            encrypted = encrypted + cipher[pos]

    return encrypted


cipher = 'bcdefghijklmnopqrstuvwxyza'

print(substitution_cipher('hello', cipher))

