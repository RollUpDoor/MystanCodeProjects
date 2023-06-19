"""
File: extension1_MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()

    if not front_is_clear():
        pick_beeper()
    else:
        pick_beeper()
        move()
    if not front_is_clear():
        turn_around()
    else:
        pass

    while not on_beeper():
        move()





def turn_around():
    turn_left()
    turn_left()






# def check_beeper():
#     """
#     Check if Karel can pick up the beeper she is stepping on.
#     """
#     move()
#     if on_beeper():
#         turn_around()
#         move()













# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
