"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	1. Show "Let's flip a coin!" first
	2. input the number of runs
	3. random show [H, T]
	"""
	print("Let's flip a coin!")
	num = int(input("Number of runs: "))
	n1 = r.choice(['H', 'T'])

	a = n1
	b = n1
	c1 = 1  # count if I have continue results (H or T)
	c2 = 0  # count how many groups of continue results I have
	while num != c2:  # hasn't reach the number of runs input by users.
		n2 = r.choice(['H', 'T'])

		if a == n2:
			c1 += 1  # we have the continue results, like TT or HH
			a = n2
			b = b + a
		else:
			if c1 >= 2:  # if c1 < 2  means there's no any continue results. ( the result will be like THTH)
				c2 += 1
				c1 = 1  # reset c1
				a = n2
				b = b + a
			else:
				a = n2
				b = b + a
	print(b)





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
