"""
File: string_manipulation2.py
Name: 
----------------------------
The goal of this file is to change
stancode to stanCode and show you
how to do string manipulations by
the following 3 steps:
(1) Start with an empty str
(2) Loop over the old str
(3) Concatenation
"""


def main():
	s = 'scancode'
	ans = ""
	for i in range(len(s)):
		alphabet = s[i]
		if i != 4:
			ans += alphabet
		else:
			ans += 'C'
	print(ans)



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
