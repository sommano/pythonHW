def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_position = alphabet.index(letter.lower())
    return letter_position


def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.lower() in alphabet:
        letter_position = alphabet_position(char)
        rotated_index = letter_position + rot
        changed_letter = alphabet[rotated_index % 26]

        if char.isupper() == True:
            changed_letter = changed_letter.upper()
            return changed_letter
        elif char.islower() == True:
            changed_letter = changed_letter.lower()
            return changed_letter
    else:
        return char