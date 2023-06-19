"""
File: caesar.py
Name: 皓暄
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program demonstrates the idea of caesar cipher.
    """
    s = int(input('Secret number: '))
    word = input('What\'s the ciphered string? ')
    new_word = change(word)  # to deal with the lowercase alphabet
    print(encryption(s, new_word))


def encryption(s, new_word):
    new_alphabet = ALPHABET[26-s:] + ALPHABET[:26-s]
    ans = ''
    for i in range(len(new_word)):
        if new_word[i] not in ALPHABET:
           ans = ans + new_word[i]
        else:
            ch = new_word[i]
            a = new_alphabet.find(ch)  # looking for the position of ch in the new alphabet
            ans = ans + ALPHABET[a]
    return ans


def change(word):
    """
    This function is changing the lowercase alphabet to the uppercase.
    """
    word1 = ''
    for i in range(len(word)):
        ch = word[i]
        if ch.islower():
            word1 = word1 + ch.upper()
        else:
            word1 += ch
    return word1




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
