"""
File: best_photoshop_award.py
Name: 皓暄
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 1


def main():
    """
    創作理念：我也要跟鹹蛋超人一樣加入宇宙警備隊，認真學好Python以維護宇宙的和平，保護弱勢的族群遠離入侵者和怪獸的入侵。
    """
    fig = SimpleImage('image_contest/Vivi.png')
    bg = SimpleImage('image_contest/Vivi_bg.jpg')
    bg.make_as_big_as(fig)
    ans = combine(fig, bg)
    ans.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            ave = (fig_pixel.red + fig_pixel.green + fig_pixel.blue)//3
            if fig_pixel.blue > ave*THRESHOLD:
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
