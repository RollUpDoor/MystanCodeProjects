"""
File: extension3_triangular_checker.py
Name: 皓暄
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program asks our user for input and checks if the input is an
    triangular number or not.
    """
    print('Welcome to the triangular number checker!')
    n = int(input("n: "))
    if n == EXIT:
        print('Have a good one!')
    while n != EXIT:
        check = checker(n)
        if check == True:  # 助教! 可以幫我看看這裡的毛毛蟲怎麼消失嗎? 還是我的判斷方式有瑕疵?
            print(str(n)+' is a triangular number')
        else:
            print(str(n)+' is not a triangular number')
        n = int(input("n: "))
    print('Have a good one!')


def checker(n):
    """
    param n: int >0
    return bool
    to see if there's a root for a,
    if yes the number is a triangular number
    """
    a = 1
    while a < n:
        if a*(a+1) != 2*n:
            a += 1
        else:
            return True
    return False


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
