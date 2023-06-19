"""
File: MidpointKarel.py
Name: 皓暄
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
    Karel will always be at the center of the 1st Street, with a beeper.
    """
    paving()

    # for one or two squares (moves).
    if not front_is_clear():
        # If the front is not clear after paving the road with beepers. It means it's one step way
        pass
    else:
        # If it's not an one step way, Karel can pick up a beeper
        pick_beeper()
        move()
    if not front_is_clear():
        # After moving one step forward, if the wall is in front, it means it's two steps way.
        turn_around()
    else:
        # for more than 2 moves.
        while on_beeper():
            if not front_is_clear():
                turn_around()
                pick_beeper()
            else:
                move()
        while not on_beeper():
            move()

        while on_beeper():
            # checking every beeper, which Karel picks is at the meddle or not, if not Karel will pick it up.
            move()
            if not on_beeper():
                turn_around()
                move()
                move()
                if not on_beeper():
                    turn_around()
                    move()
                    break
                else:
                    turn_around()
                    move()
                    turn_around()
                    pick_beeper()
                    move()

            else:
                turn_around()
                move()
                turn_around()
                move()


def paving():
    """
    Pre-condition: Karel is at (1,1) without beepers, facing east.
    Post-condition: Karel is at the end of the road with beepers, facing west.
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_around()


def turn_around():
    turn_left()
    turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
