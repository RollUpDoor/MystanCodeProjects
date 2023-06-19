"""
File: hailstone.py
Name: 皓暄
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone sequences.
    """
    print('This program computes Hailstone sequences.', end='\n')
    print("")
    n = int(input('Enter a number: '))
    times = 0
    while n != 1:  # after n reach 1, the while loop will stop
        times += 1  # for counting how many steps to reach 1.
        if n % 2 == 0:
            print(str(n)+' is even', end=', ')  # The 'n' here is the number user key in.
            n = even(n)
            print('so I take half: '+str(n))  # The 'n' here is the new number we got after using "even" function.
        else:
            print(str(n) + ' is odd', end=', ')  # The 'n' here is the number user key in.
            n = odd(n)
            print('so I make 3n+1: ' + str(n))  # The 'n' here is the new number we got after using "odd" function.

    print('It took '+str(times)+' steps to reach 1.')


def odd(n):
    """
    :param n: int>0
    """
    n = int(n*3+1)
    return n


def even(n):
    """
    :param n: int>0
    """
    n = int(n/2)
    return n


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
