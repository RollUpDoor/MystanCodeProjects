"""
File: file_reading.py
Name:
---------------------------
This file shows how we can open and
print text files through Python code
"""
import random

NUM_ROLLS = 15
def main():
	roll = random.randrange(1, 7)
	print('Rolls: ' + str(roll))
	check = roll
	cnt = 0

	for i in range(NUM_ROLLS - 1):
		roll = random.randrange(1, 7)
		print("Rolls: " + str(roll))

		if check == roll:
			cnt += 1
		else:
			cnt = cnt

		check = roll

	print('Number of runs: ' + str(cnt))

	# filepath = "text/JerrySecret4.txt"
	# with open(filepath, 'r') as f:
	# 	for line in f:
	# 		print(line, end='')

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
