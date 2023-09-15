"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_list =[]

def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')

    read_dictionary(FILE)
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        key_in = input("Find anagrams for: ")
        if key_in == -1:
            break
        else:
            print('Searching...')
            find_ana_list=find_anagrams(key_in)
            print(find_ana_list)


def read_dictionary(FILE):
    with open(FILE, 'r') as f:
        for line in f:
            token_list = line.split('\n')
            word = token_list[0].strip()
            word_list.append(word)

def find_anagrams(s):
    """
    :param s:
    :return:
    """
    pass


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
