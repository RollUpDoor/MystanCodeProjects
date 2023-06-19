"""
File: mirror_lake.py
Name:皓暄
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: mt-rainier
    :return: reflected
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    b_img = SimpleImage.blank(original_mt.width*1, original_mt.height*2)

    for x in range(original_mt.width):
        for y in range(original_mt.height):
            reflected_pixel = original_mt.get_pixel(x, y)
            blank_pixel = b_img.get_pixel(x, y)
            blank_pixel.red = reflected_pixel.red
            blank_pixel.green = reflected_pixel.green
            blank_pixel.blue = reflected_pixel.blue

            mirrored_blank_pixel = b_img.get_pixel(x, b_img.height-1-y)
            mirrored_blank_pixel.red = reflected_pixel.red
            mirrored_blank_pixel.green = reflected_pixel.green
            mirrored_blank_pixel.blue = reflected_pixel.blue

    return b_img


def main():
    """
    Make a reflection of mountain
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
