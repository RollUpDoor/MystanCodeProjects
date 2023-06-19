"""
File: quadratic_solver.py
Name:皓暄
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	:param a: int a>=<0
	:param b: int b>=<0
	:param c: int c>=<0
	:return: int [(-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a ] and [(-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a]
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	if (b**2-4*a*c) > 0:
		print('Two roots: '+str(ans_one(a, b, c))+' , '+str(ans_two(a, b, c)))
	elif (b**2-4*a*c) == 0:
		print('One root: ' + str(ans_two(a, b, c)))
	else:
		print('No real roots')


def ans_one(a, b, c):
	x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
	return x1


def ans_two(a, b, c):
	x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
	return x2


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
