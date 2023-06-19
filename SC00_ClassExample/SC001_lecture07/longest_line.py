"""
File: longest_line.py
Name:
---------------------------
This file shows how we can find
the longest line in romeojuliet.txt
through Python code
"""

# This constant shows the file path to romeojuliet.txt
FILEPATH = 'text/romeojuliet.txt'


def main():
	with open(FILEPATH, 'r') as f :
		longest_line =''
		longest_count = 0
		for line in f:
			if len(line) > len(longest_line):
				longest_line = line
		print(longest_line)


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
