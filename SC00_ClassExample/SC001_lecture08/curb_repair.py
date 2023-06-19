"""
File: curb_repair.py
Name:
-------------------------------
This program shows how to detect red pixels
of curb and change them into gray scale, making
the curb area be considered as an available parking space!
"""
from simpleimage import SimpleImage
THRESHOLD = 1.2


def main():
    img = SimpleImage("images/curb.png")
    # 紅色大於平均就代表偏紅色
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue)//3
        if pixel.red > avg*THRESHOLD:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
