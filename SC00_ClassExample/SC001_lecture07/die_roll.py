"""
File: die_roll.py
Name:
---------------------
This file uses random to simulate
4 dice roll for shi-ba-la
"""

import random

# This constant controls the number of players for the game
NUM_PLAYER = 5

# This constant shows the number of dice for shi-ba-la
NUM_DICE = 4


def main():
    """
    This program uses random to simulate real dice roll for shi-ba-la
    """
    random.seed()
    for i in range(NUM_PLAYER):
        rolls = ''
        for j in range(NUM_DICE):
            roll = random.randrange(1, 7)
            rolls += str(roll)
        print(rolls)


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
