# Vigenere Cipher (Polyalphabetic Substitution Cipher)
 2. # http://inventwithpython.com/hacking (BSD Licensed)
 3.
 4. import pyperclip
 5.
 6. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 7.
 8. def main():
 9.     # This text can be copy/pasted from http://invpy.com/vigenereCipher.py
10.     myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted."""
11.     myKey = 'ASIMOV'
12.     myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
13.
14.     if myMode == 'encrypt':
15.         translated = encryptMessage(myKey, myMessage)
16.     elif myMode == 'decrypt':
17.         translated = decryptMessage(myKey, myMessage)
18.
19.     print('%sed message:' % (myMode.title()))
20.     print(translated)
21.     pyperclip.copy(translated)
22.     print()
23.     print('The message has been copied to the clipboard.')
24.
25.
26. def encryptMessage(key, message):
27.     return translateMessage(key, message, 'encrypt')
28.
29.
30. def decryptMessage(key, message):
31.     return translateMessage(key, message, 'decrypt')
32.
33.
34. def translateMessage(key, message, mode):
35.     translated = [] # stores the encrypted/decrypted message string
36.
37.     keyIndex = 0
38.     key = key.upper()
39.
40.     for symbol in message: # loop through each character in message
41.         num = LETTERS.find(symbol.upper())
42.         if num != -1: # -1 means symbol.upper() was not found in LETTERS
43.             if mode == 'encrypt':
44.                 num += LETTERS.find(key[keyIndex]) # add if encrypting
45.             elif mode == 'decrypt':
46.                 num -= LETTERS.find(key[keyIndex]) # subtract if decrypting
47.
48.             num %= len(LETTERS) # handle the potential wrap-around
49.
50.             # add the encrypted/decrypted symbol to the end of translated.
51.             if symbol.isupper():
52.                 translated.append(LETTERS[num])
53.             elif symbol.islower():
54.                 translated.append(LETTERS[num].lower())
55.
56.             keyIndex += 1 # move to the next letter in the key
57.             if keyIndex == len(key):
58.                 keyIndex = 0
59.         else:
60.             # The symbol was not in LETTERS, so add it to translated as is.
61.             translated.append(symbol)
62.
63.     return ''.join(translated)
64.
65.
66. # If vigenereCipher.py is run (instead of imported as a module) call
67. # the main() function.
68. if __name__ == '__main__':
69.     main()