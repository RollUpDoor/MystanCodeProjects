"""
File: bouncing_ball
Name: 皓暄
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 30
GRAVITY = 1
SIZE = 10
REDUCE = 0.9
START_X = 30
START_Y = 40
# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = 0
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)  # create a ball
    window.add(ball)  # display
    ball.filled = True
    onmouseclicked(ball_move)  # click mouse and the ball drops


def ball_move(mouse):
    global ball, count
    if count < 3:  # stop when clicking more than 3 times
        vy = 0
        count += 1
        while True:
            ball.move(VX, vy)
            vy += GRAVITY  # vy1 =1, vy2=2...
            pause(DELAY)
            if ball.y+SIZE >= window.height:  # rebound
                vy = -vy*REDUCE
            if ball.x >= window.width:  # reset ball
                ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                window.add(ball)
                ball.filled = True
                break  # back to the beginning






if __name__ == "__main__":
    main()
