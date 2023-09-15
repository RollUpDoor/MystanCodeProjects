"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
EXIT = -1


def main():
    """
    1. Input the course number.
    2. Input the score.
    3. input "-1" --> show the maximum, minimum, and average among all the inputs
    """
    max001 = max101 = -float('inf')
    min001 = min101 = float('inf')
    count001 = count101 = 0
    sc101_sum = sc001_sum = 0
    while True:
        course = input('Which class? ')
        course = course.upper()
        if course == str(EXIT):
            if count001 == 0 and count101 == 0:
                print('No class scores were entered')
            elif count001 != 0 and count101 != 0:
                print('=============SC001=============')
                print('Max (001): ' + str(max001))
                print('Min (001): ' + str(min001))
                print('Avg (001): ' + str(sc001_sum/count001))
                print('=============SC101=============')
                print('Max (101): ' + str(max101))
                print('Min (101): ' + str(min101))
                print('Avg (101): ' + str(sc101_sum/count101))
            elif count001 > 0 and count101 == 0:
                print('=============SC001=============')
                print('Max (001): ' + str(max001))
                print('Min (001): ' + str(min001))
                print('Avg (001): ' + str(sc001_sum / count001))
                print('=============SC101=============')
                print('No score for SC101')
            else:
                print('=============SC001=============')
                print('No score for SC001')
                print('=============SC101=============')
                print('Max (101): ' + str(max101))
                print('Min (101): ' + str(min101))
                print('Avg (101): ' + str(sc101_sum / count101))
            break
        elif course != 'SC101' and course != 'SC001':
            print("Please input the correct course name (SC101 or SC001) or -1 to EXIT")
        else:
            score = int(input('Score: '))
            if course == 'SC001':
                sc001_sum += score
                count001 += 1
                if score > max001:
                    max001 = score
                if score < min001:
                    min001 = score
            if course == 'SC101':
                sc101_sum += score
                count101 += 1
                if score > max101:
                    max101 = score
                if score < min001:
                    min101 = score





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
