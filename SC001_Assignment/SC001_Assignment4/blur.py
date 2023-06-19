"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: smiley-face
    :return: blur_face
    """
    img = SimpleImage("images/smiley-face.png")
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)


    # Loop over the picture

    for x in range(img.width):
        for y in range(img.height):
            new_img_pixel = new_img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.

                pixel_2 = img.get_pixel(x + 1, y)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x + 1, y + 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_2.red + pixel_7.red + pixel_8.red + pixel_9.red) / 4
                new_g = (pixel_2.green + pixel_7.green + pixel_8.green + pixel_9.green) / 4
                new_b = (pixel_2.blue + pixel_7.blue + pixel_8.blue + pixel_9.blue) / 4

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.

                pixel_1 = img.get_pixel(x - 1, y)
                pixel_6 = img.get_pixel(x - 1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_1.red + pixel_6.red + pixel_7.red + pixel_9.red) / 4
                new_g = (pixel_1.green + pixel_6.green + pixel_7.green + pixel_9.green) / 4
                new_b = (pixel_1.blue + pixel_6.blue + pixel_7.blue + pixel_9.blue) / 4

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image

                pixel_2 = img.get_pixel(x + 1, y)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_2.red + pixel_4.red + pixel_5.red + pixel_9.red) / 4
                new_g = (pixel_2.green + pixel_4.green + pixel_5.green + pixel_9.green) / 4
                new_b = (pixel_2.blue + pixel_4.blue + pixel_5.blue + pixel_9.blue) / 4

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image

                pixel_1 = img.get_pixel(x - 1, y)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_1.red + pixel_3.red + pixel_4.red + pixel_9.red) / 4
                new_g = (pixel_1.green + pixel_3.green + pixel_4.green + pixel_9.green) / 4
                new_b = (pixel_1.blue + pixel_3.blue + pixel_4.blue + pixel_9.blue) / 4

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)

                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x + 1, y)
                pixel_6 = img.get_pixel(x - 1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x + 1, y + 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_1.red + pixel_2.red + pixel_6.red + pixel_7.red + pixel_8.red + pixel_9.red) / 6
                new_g = (pixel_1.green + pixel_2.green + pixel_6.green + pixel_7.green + pixel_8.green + pixel_9.green) / 6
                new_b = (pixel_1.blue + pixel_2.blue + pixel_6.blue + pixel_7.blue + pixel_8.blue + pixel_9.blue) / 6

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)

                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x + 1, y)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red + pixel_9.red) / 6
                new_g = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green + pixel_9.green) / 6
                new_b = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue + pixel_9.blue) / 6

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)

                pixel_2 = img.get_pixel(x + 1, y)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x + 1, y + 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_2.red + pixel_4.red + pixel_5.red + pixel_7.red + pixel_8.red + pixel_9.red) / 6
                new_g = (pixel_2.green + pixel_4.green + pixel_5.green + pixel_7.green + pixel_8.green + pixel_9.green) / 6
                new_b = (pixel_2.blue + pixel_4.blue + pixel_5.blue + pixel_7.blue + pixel_8.blue + pixel_9.blue) / 6

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)

                pixel_1 = img.get_pixel(x - 1, y)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_6 = img.get_pixel(x - 1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = (pixel_1.red + pixel_3.red + pixel_4.red + pixel_6.red + pixel_7.red + pixel_9.red) / 6
                new_g = (pixel_1.green + pixel_3.green + pixel_4.green + pixel_6.green + pixel_7.green + pixel_9.green) / 6
                new_b = (pixel_1.blue + pixel_3.blue + pixel_4.blue + pixel_6.blue + pixel_7.blue + pixel_9.blue) / 6

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

            else:
                # Inner pixels.

                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x + 1, y)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                pixel_6 = img.get_pixel(x - 1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x + 1, y + 1)
                pixel_9 = img.get_pixel(x, y)

                new_r = ((pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red
                          + pixel_6.red + pixel_7.red + pixel_8.red + pixel_9.red) / 9)
                new_g = ((pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green
                          + pixel_6.green + pixel_7.green + pixel_8.green + pixel_9.green) / 9)
                new_b = ((pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue
                          + pixel_6.blue + pixel_7.blue + pixel_8.blue + pixel_9.blue) / 9)

                new_img_pixel.red = new_r
                new_img_pixel.green = new_g
                new_img_pixel.blue = new_b

    return new_img


def main():
    """
    It makes picture blur
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
