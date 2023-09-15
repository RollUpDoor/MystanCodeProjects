"""
File: CollectNewspaperKarel.py
Name: 皓暄
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

#from karel.stanfordkarel import *


def main():
    """
    Karel will bring the news paper, which is at (6,3) back to (3,4).
    """




#     go_get_newspaper()
#     go_home()
#
#
# def go_get_newspaper():
#     """
#     Pre-condition: Karel is at home (3,4), facing East.
#     Post-condition: Karel is at (6,3) and pick up the news paper, facing East.
#     """
#     turn_right()
#     move()
#     turn_left()
#     while not on_beeper():
#         move()
#     pick_beeper()
#
#
# def turn_right():
#     # turn left 3 times
#     for i in range(3):
#         turn_left()
#
#
# def go_home():
#     """
#     Pre-condition: Karel is at (6,3) and pick up the news paper, facing East.
#     Post-condition: Karel is at home (3,4) with news paper, facing East.
#     """
#     turn_around()
#     while front_is_clear():
#         move()
#     turn_right()
#     move()
#     turn_right()
#
#
# def turn_around():
#     # turn left 2 times
#     for i in range(2):
#         turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
