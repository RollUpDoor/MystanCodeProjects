"""
File: flip_horizontally.py
Name: 
------------------------------------
This program shows how to create an empty SimpleImage
as well as making a mirrored image of poppy.png by
replacing pixels on blank new canvas by ones on poppy.png
"""


from simpleimage import SimpleImage


def main():
    img = SimpleImage("images/poppy.png")
    img.show()

    b_img = SimpleImage.blank(img.width*2, img.height*2)
    b_img.show()

    for x in range(img.width):
        for y in range(img.height):
            colored_pixel = img.get_pixel(x, y)
            blank_pixel = b_img.get_pixel(x, y)
            blank_pixel.red = colored_pixel.red
            blank_pixel.green = colored_pixel.green
            blank_pixel.blue = colored_pixel.blue

            mirrored_blank_pixel = b_img.get_pixel(b_img.width-1-x, y)
            mirrored_blank_pixel.red = colored_pixel.red
            mirrored_blank_pixel.green = colored_pixel.green
            mirrored_blank_pixel.blue = colored_pixel.blue
    b_img.show()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
