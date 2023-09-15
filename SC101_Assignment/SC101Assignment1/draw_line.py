"""
File: draw_line.py
Name: 皓暄
-------------------------
1. 1st click --> a dot
2. 2nd click --> a line
...repeatedly
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10
# Global variable
window = GWindow()
switcher = 0
dot = 0
def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(a_dot)  # 1st click to make a dot


def a_dot(click):
    global switcher, dot
    if switcher == 0:
        dot = GOval(SIZE, SIZE, x=click.x-SIZE/2, y=click.y-SIZE/2)  # create a dot, appears where the mouse clicks
        window.add(dot)  # display
        switcher = 1  # turn on
    else:
        line = GLine(x0=dot.x+SIZE/2, y0=dot.y+SIZE/2, x1=click.x, y1=click.y)  # create a line from the center of the circle to the new mouse click position
        window.add(line)
        window.remove(dot)
        switcher = 0  # turn off



if __name__ == "__main__":
    main()
