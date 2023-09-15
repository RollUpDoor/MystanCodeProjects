"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the image which will be blurred
    :return: a blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)  # create a new blank image, which is as big as the original one

    # Iterate over each pixel in the old img
    for y in range(img.height):
        for x in range(img.width):
            # initialize the variables that will be used to calculate the average RGB
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            new_img_pixel = new_img.get_pixel(x, y)
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i  # if x==0, i ==-1, and then pixel_x == -1 (does not exist, will be screened by 'if')
                    pixel_y = y + j

                    # If the surrounding pixel is within the bounds of the old image or not.
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            red_avg = r_sum // count
            green_avg = g_sum // count
            blue_avg = b_sum // count
            new_img_pixel.red = red_avg
            new_img_pixel.green = green_avg
            new_img_pixel.blue = blue_avg
    return new_img


def main():
    """
    open the photo, show the old_img
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
