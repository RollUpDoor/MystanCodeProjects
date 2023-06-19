"""
File: rocket.py
Name: 皓暄
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    for building a rocket and user can adjust the size by key in the number.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ", end='')
        for j in range(i+1):
            print("/", end='')
        for j in range(i+1):
            print("\\", end='')
        print("")


def belt():
    print("+", end='')
    for i in range(2*SIZE):
        print("=", end='')
    print("+", end='\n')


def upper():
    for i in range(SIZE):
        print("|", end='')
        for j in range(SIZE-i-1):
            print(".", end='')
        for j in range(i+1):
            print("/", end='')
            print("\\", end='')
        for j in range(SIZE-i-1):
            print(".", end='')
        print("|")


def lower():
    for k in range(SIZE):
        print("|", end='')
        for j in range(k):
            print(".", end='')
        for j in range(SIZE-k):
            print("\\", end='')
            print("/", end='')
        for j in range(k):
            print(".", end='')
        print("|")














# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
