"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        # Game Over
        if lives == 0:
            break
        if graphics.brick_num == 0:
            break
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            graphics.reset_ball()
            if lives == 2:
                graphics.remove_life3()
            elif lives == 1:
                graphics.remove_life2()
            else:
                graphics.remove_life1()
        graphics.handle_wall_collisions()
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)

        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
