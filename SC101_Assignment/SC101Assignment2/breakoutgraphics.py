"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
# global variable
switcher = True
score = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_offset = PADDLE_OFFSET
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.window.add(self.paddle, x=window_width/2-paddle_width/2, y=window_height-paddle_offset)
        self.paddle.filled = True

        # Label
        self.label = GLabel('LIVES: ')
        self.window.add(self.label, x=5, y=self.label.height+10)
        self.label_live1 = GLabel('❤')
        self.label_live1.font = '-10'
        self.window.add(self.label_live1, x=7+self.label.width, y=self.label.height+10)
        self.label_live2 = GLabel('❤')
        self.label_live2.font = '-10'
        self.window.add(self.label_live2, x=9+self.label.width+self.label_live1.width, y=self.label.height + 10)
        self.label_live3 = GLabel('❤')
        self.label_live3.font = '-10'
        self.window.add(self.label_live3, x=11+self.label.width+self.label_live1.width+self.label_live2.width, y=self.label.height + 10)
        self.score = GLabel("SCORE: ")
        self.window.add(self.score, x=self.label_live3.x+30, y=self.label.height + 10)
        self.score.text = "SCORE: " + str(score)


        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2+ball_radius)
        self.ball.filled = True

        # Initialize velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # num of bricks
        self.brick_num = brick_rows * brick_cols

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Draw bricks
        x_s = 0
        y_s = brick_offset
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(width=brick_width, height=brick_height, x=x_s, y=y_s)
                self.bricks.filled = True
                if i < 3:
                    self.bricks.fill_color = 'red'  # rows 1, 2 --> Red
                elif i < 5:
                    self.bricks.fill_color = 'orange'  # rows 3, 4 --> Orange
                elif i < 7:
                    self.bricks.fill_color = 'yellow'  # rows 5, 6 --> Yellow
                elif i < 9:
                    self.bricks.fill_color = 'green'  # rows 7, 8 --> Green
                else:
                    self.bricks.fill_color = 'blue'  # row 9, 10 --> Blue

                self.window.add(self.bricks)
                x_s += brick_width + brick_spacing
            x_s = 0  # new row to reset x_s
            y_s += brick_height + brick_spacing

    def paddle_move(self, event):
        if event.x <= 0:
            self.paddle.x = 0
        elif event.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x

    """
    The following codes are about the ball
    """
    def set_ball_position(self):
        self.ball.x = self.window.width / 2 - self.ball.width
        self.ball.y = self.window.height / 2 - self.ball.height

    def ball_move(self, event):
        global switcher
        if switcher:
            switcher = False
            self.set_ball_velocity()

    # Default initial velocity for the ball
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Getter for ball dx
    def get_dx(self):
        return self.__dx

    # Getter for ball dy
    def get_dy(self):
        return self.__dy

    def reset_ball(self):
        """
        Sets the ball in the the graphical window (when lives>=0)
        """
        global switcher
        self.set_ball_position()
        self.__dx = 0
        self.__dy = 0
        switcher = True

    """
    detect corner hit: chang x and y
    """
    def handle_wall_collisions(self):
        # set 4 corners var. to check for collision
        ball_corner1 = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_corner2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        ball_corner3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        ball_corner4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y+self.ball.height)
        # wall (right and left side)
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        # ceiling
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        # hit the paddle
        if self.ball.y > self.window.height/2:
            if ball_corner1 or ball_corner2 or ball_corner3 or ball_corner4 is not None:
                self.__dy = -self.__dy
        else:
            global score
            # hit the bricks (checking the upper right and left corners)
            if ball_corner1 or ball_corner2 is not None:
                self.__dy = -self.__dy
                self.window.remove(ball_corner1)
                self.window.remove(ball_corner2)
                score += 1
                self.score.text = "SCORE: "+str(score)
            # hit the bricks (checking the lower right and left corners)
            elif ball_corner3 or ball_corner4 is not None:
                self.__dy = -self.__dy
                self.window.remove(ball_corner3)
                self.window.remove(ball_corner4)
                score += 1
                self.score.text = "SCORE: " + str(score)
            # hit the bricks (checking the lower and upper left corners)
            elif ball_corner1 or ball_corner3 is not None:
                self.__dx = -self.__dx
                self.window.remove(ball_corner1)
                self.window.remove(ball_corner3)
                score += 1
                self.score.text = "SCORE: " + str(score)
            # hit the bricks (checking the lower and upper right corners)
            else:
                if ball_corner2 or ball_corner4 is not None:
                    self.__dx = -self.__dx
                    self.window.remove(ball_corner2)
                    self.window.remove(ball_corner4)
                    score += 1
                    self.score.text = "SCORE: " + str(score)

    def remove_life3(self):
        self.window.remove(self.label_live3)

    def remove_life2(self):
        self.window.remove(self.label_live2)

    def remove_life1(self):
        self.window.remove(self.label_live1)

