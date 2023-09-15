"""
File: StoneMasonKarel.py
Name: 皓暄
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel is going to build pillars for all the arches,
    and the distance between each pillar is always three blocks away.
    *The height of pillars needs to be considered.*
    """
    while front_is_clear():
        build_pillars()
        move_back()
        move_to_pillars()
    build_pillars()
    move_back()
    # move_to_pillars()


def build_pillars():
    """
    Pre-condition: Karel is at the ground floor, facing East.
    Post-condition: Karel is at the top floor, facing South.
    """
    turn_left()
    # facing north, Karel starts to go.
    while front_is_clear():
        # consider the height of pillars
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()
    turn_around()


def move_back():
    """
    Pre-condition: Karel is at the top floor, facing South.
    Post-condition: Karel is at the ground floor of pillar, facing East.
    """
    while front_is_clear():
        move()
    turn_left()


def move_to_pillars():
    """
    pre-condition: Karel is at the ground floor of pillar, facing East.
    Post-condition: Karel is at the ground floor of the next pillar, facing East.
    """
    if front_is_clear():
        for i in range(4):
            move()


def turn_around():
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
