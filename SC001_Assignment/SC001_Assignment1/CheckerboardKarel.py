"""
File: CheckerboardKarel.py
Name: 皓暄
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    The beepers should be arranged at intervals into a checkerboard state
    in any rectangular or square space.
    """

    while front_is_clear():
        move()
        if not front_is_clear():
            turn_left()
            while on_beeper():
                pick_beeper()
    else:
        move()

    # Karel must put a beeper at the beginning (1,1)
#     start_put_beeper()
#     while facing_east():
#         go_home()
#         if on_beeper():
#             check_next_line()
#             start_no_put_beeper()
#         else:
#             check_next_line()
#             start_put_beeper()
#
#
# def start_no_put_beeper():
#     """
#     Pre-condition: Karel stands at the beginning of the line,facing East and she doesn't need to put beeper first.
#     Post-condition: Karel stands at the end of the line, facing East.
#     """
#     if front_is_clear():
#         move()
#         put_beeper()
#     while front_is_clear():
#         move()
#         if front_is_clear():
#             move()
#             put_beeper()
#
#
# def start_put_beeper():
#     """
#     Pre-condition: Karel stands at the beginning of the line, facing East and she needs to put a beeper first.
#     Post-condition: Karel stands at the end of the line, facing East.
#     """
#     if facing_east():
#         put_beeper()
#     while front_is_clear():
#         move()
#         if front_is_clear():
#             move()
#             put_beeper()
#
#
# def go_home():
#     """
#     Pre-condition: Karel is at the end of the line, facing East.
#     Post_condition: Karel is back to home (1,Y), facing west.
#     """
#     if not front_is_clear():
#         for i in range(2):
#             turn_left()
#     while front_is_clear():
#         move()
#
#
# def check_next_line():
#     """
#     Pre-condition: Karel is back to home (1,Y), facing west.
#     Post-condition: Karel stands at the beginning of the line, facing East.
#     """
#     turn_right()
#     if front_is_clear():
#         move()
#         turn_right()
#
#
# def turn_right():
#     for i in range(3):
#         turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
