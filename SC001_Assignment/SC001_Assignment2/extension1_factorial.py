"""
File: extension1_factioral.py
Name: 皓暄
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	The program finds the factorial
	"""
	print('Welcome to stanCode factorial master!')
	a = int(input('Give me a number, and I will list the answer of factorial: '))

	while True:
		if a == EXIT:
			print("- - - - - - See ya! - - - - - -")
			break
		elif a == 0:
			print('Ans: 1')

		else:
			ans = 1
			for i in range(1, a+1):  # including the lower bound, not including the upper bound
				ans *= i  # e.g.: a==6, so the range of i is (1,7)--> ans = 1*2*3*4*5*6
			print('Ans: '+str(ans))
		a = int(input('Give me a number, and I will list the answer of factorial: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()