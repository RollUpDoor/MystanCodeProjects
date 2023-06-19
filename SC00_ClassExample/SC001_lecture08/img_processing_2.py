"""
File: img_processing_2.py
Name:
-------------------------------
This file contains 2 image processing algorithms:
(1.) left_half_darken
(2.) gray_scale
"""


from simpleimage import SimpleImage


def main():
    """
    This file contains 2 image processing algorithms:
    left_half_darken and gray_scale
    """
    # filepath = 'images/stop.png'
    img = SimpleImage('images/stop.png')
    img.show()


    # half_dark_img = left_half_darken('images/stop.png')
    # half_dark_img.show()



    gray_scale_img = gray_scale('images/stop.png')
    gray_scale_img.show()


def left_half_darken(filepath):  # 丟檔案路徑進來
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return img: SimpleImage, the image with half horizontal area darken
    """

    darken_img = SimpleImage(filepath)
    for x in range(darken_img.width):
        for y in range(darken_img.height):
            pixel = darken_img.get_pixel(x, y)
            if x < darken_img.width/2:
                if y < darken_img.height/2:
                # darken1
                    pixel.red = pixel.red // 2
                    pixel.green = pixel.green // 2
                    pixel.blue = pixel.blue // 2

            if x > darken_img.width/2:
                if y > darken_img.height/2:
                    # dark4
                    pixel.red = pixel.red // 2
                    pixel.green = pixel.green // 2
                    pixel.blue = pixel.blue // 2

            if x > darken_img.width / 2:
                if y < darken_img.height / 2:
                    # bright2
                    pixel.red = pixel.red * 2
                    pixel.green = pixel.green * 2
                    pixel.blue = pixel.blue * 2

            if x < darken_img.width / 2:
                if y > darken_img.height / 2:
                    # bright3
                    pixel.red = pixel.red * 2
                    pixel.green = pixel.green * 2
                    pixel.blue = pixel.blue * 2

    return darken_img


def gray_scale(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return: SimpleImage, gray scaled image
    """
    gray_img = SimpleImage(filepath)
    for pixel in gray_img:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        pixel.red = avg  # 也可等於 pixel.red 紅色物品資訊，會以回色為主的灰階
        pixel.green = avg
        pixel.bleu = avg
    return gray_img


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
