"""
File: hangman.py
Name: 皓暄
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Guessing the word. ^^
    """
    num = random_word()
    x = N_TURNS
    ans = ''

    for i in range(len(num)):
        ans = ans + "-"

    print("Welcome to the game")
    print("The word looks like " + ans)

    while x > 0 and ans[i] == "-":
        key = input("Your Guess: ")
        key = key.upper()

        if len(key) > 1 or not key.isalpha():
            print("Illegal format")

        elif key in num:
            for i in range(len(num)):
                if key == num[i]:
                    ans = ans[:i] + key + ans[i + 1:]
                else:
                    ans = ans
            if '-' not in ans:
                print('You are correct!')
                print('You win!!')
                print('The word was: ' + num)
                break
            print('You are correct!')
            print('The word looks like ' + ans)
            print('You have ' + str(x) + " wrong guesses left.")

        else:
            x -= 1
            print("There is no " + key + "'s in the word.")
            if x == 0:
                print('You are completely hung :( ')
                print('The word was: ' + num)
                break
            print('The word looks like ' + ans)
            print('You have ' + str(x) + " wrong guesses left.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
