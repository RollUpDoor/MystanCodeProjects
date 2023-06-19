"""
File: weather_master.py
Name: 皓暄
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100
TEMP = 16  # for setting the cold day temperature


def main():
	"""
	This program finds the highest and lowest temperature
	, averages and days of cold weather among user inputs.
	"""
	total = 0
	n = 0
	cold_days = 0
	print('stanCode "Weather Master 4.0"!')
	weather = int(input('Next Temperature: (or ' + str(EXIT)+' to quit)? '))
	if weather == EXIT:  # EXIT the program
		print('No temperatures were entered.')
	else:
		maximum = weather
		minimum = weather
		while True:
			total = total + weather
			n += 1
			weather = int(input('Next Temperature: (or ' + str(EXIT)+' to quit)? '))
			if weather == EXIT:
				break
			if weather > maximum:
				maximum = weather  # replacing the maximum number
			if weather < minimum:
				minimum = weather  # replacing the minimum number
			if weather < TEMP:
				cold_days += 1  # counting the days which temp. is lower than 'TEMP'
		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(total/n))
		print(str(cold_days)+' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
