"""
File: fire.py
Name: 皓暄
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: greenland-fire.png
    :return: img_fire
    """
    img = SimpleImage("images/greenland-fire.png")
    for pixel in img:
        ave = (pixel.red + pixel.green + pixel.blue) //3
        if pixel.red > ave*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = ave
            pixel.green = ave
            pixel.blue = ave

    return img


def main():
    """
    It shows the place where fires are taking in
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
