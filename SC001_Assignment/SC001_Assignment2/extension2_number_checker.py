"""
File: extension2_number_checker.py
Name: 皓暄
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program asks our user for input and checks if the input is a
    perfect number、deficient number or an abundant number.
    """
    print('Welcome to the number checker!')
    a = int(input('n: '))
    if a == EXIT:
        print('Have a good one!')
    while a != EXIT:
        add = checker(a)  # execute the function checker and get the return answer
        if add == a:
            print(str(a)+' is a perfect number')
        elif add > a:
            print(str(a) + ' is a abundant number')
        else:
            print(str(a) + ' is a deficient number')
        a = int(input('n: '))
    print('Have a good one!')


def checker(a):
    """
    param a: int>0
    return add: int>0
    It will return the sum of all its factors(aside from the number itself).
    """
    add = 0
    for i in range(1, a+1):
        if a % i == 0:
            add = add + i
    add = add - a  # the sum of all its factors aside from itself
    return add


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
