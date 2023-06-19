"""
File: prime_checker.py
Name: 皓暄
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program finds the number which users key in is a prime number or not.
	"""
	print('Welcome to the prime checker!')
	n = int(input('n: '))
	if n == EXIT:
		print('Have a good one!')

	while n != EXIT:
		prime = check_prime(n)  # get the result of function check_prime(n)
		if prime:
			print(str(n)+' is not a prime number.')
		else:
			print(str(n) + ' is a prime number.')
		n = int(input('n: '))
	print('Have a good one!')


def check_prime(n):
	"""
	:param n: int >0
	return: bool, if n is prime or not

	prime number is a whole number greater than 1 that cannot be exactly divided by any whole number
	other than itself and 1
	"""
	for i in range(2, n-1):  # i starts with 2, and end with the 'n'-1
		if n % (i) == 0:  # divided by any whole number other than itself and 1
			return True  # return True while n is not a prime number


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
