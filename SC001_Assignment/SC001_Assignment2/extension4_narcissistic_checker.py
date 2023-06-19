"""
File: extension4_narcissistic_checker.py
Name: 皓暄
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program asks our user for input and checks if the input is a
    narcissistic number or not.
    """
    print('Welcome to the narcissistic checker!')
    n = int(input("n: "))
    if n == EXIT:
        print('Have a good one!')
    while n != EXIT:
        check = checker(n)
        if check == True:
            print(str(n) + ' is a narcissistic number')
        else:
            print(str(n) + ' is not a narcissistic number')
        n = int(input("n: "))
    print('Have a good one!')


def checker(n):
    """
    param n: int >0
    return bool
    """
    a = n // 1 % 10  # one
    b = n // 10 % 10  # ten
    c = n // 100 % 10  # hundred
    d = n // 1000 % 10  # thousand
    e = n // 10000 % 10  # ten thousand
    x = 0  # power
    ans = 0

    while ans < n:
        if x < n:  # adding a condition for dealing with the number, if every unit is "1" (e.g.: 1、10、11、111...)
            ans = a**x + b**x + c**x + d**x + e**x
            x += 1
        else:
            return False
    if ans == n:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
