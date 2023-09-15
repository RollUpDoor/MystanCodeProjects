"""
File: babygraphics.py
Name: 皓暄
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = ((width-GRAPH_MARGIN_SIZE*2)/len(YEARS)*year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # construct horizontal lines on canvas
    # celling
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE),
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), width=LINE_WIDTH)
    # construct straight lines
    # 我有幾個年
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill='black')
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT, text=str(YEARS[i]),
                           anchor=tkinter.SW, fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    color = 0  # 用來初始化顏色，他會去追蹤我要用哪個顏色去畫曲線和文字的顏色
    for name in lookup_names:  # for loop 會把lookup_name list 裡面的每個名字執行下面的程式
        data_list = []  # 一個空的 List，會用來儲存每個名字那年份的位置(x,y)
        for year in range(len(YEARS)):
            year_data = []  # 一個空的 List儲存當前年份的xy

            # 計算x座標
            x_coordinate = get_x_coordinate(CANVAS_WIDTH, year)
            # 把當前的年x座標加入 year_data list
            year_data.append(x_coordinate)

            """
            檢查我現在的年是不是在我 nmae_data字典裏面，如果是的話代表我的名字在當年的排名是存在的
            name_data[name][year]
            """
            if str(YEARS[year]) in name_data[name]:
                rank = int(name_data[name][str(YEARS[year])])  # 取出rank
                y_coordinate = (rank * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)) // MAX_RANK + GRAPH_MARGIN_SIZE
            else:
                # If the rank doesn't exist, set a default y-coordinate
                y_coordinate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            year_data.append(y_coordinate)  # Add the y-coordinate to the year_data list
            data_list.append(year_data)  # Add the year_data to the data_list

            # Get the rank in string format or "*" if it doesn't exist
            if str(YEARS[year]) in name_data[name]:
                rank = str(rank)
            else:
                rank = "*"

            # Create the text on the canvas
            text = str(name) + " " + rank
            anchor_position = tkinter.SW  # Set the anchor position to the bottom-left corner of the text
            fill_color = COLORS[color]  # Get the color for the tex
            canvas.create_text(x_coordinate + TEXT_DX, y_coordinate, text=text, anchor=anchor_position, fill=fill_color)

        # Check over the positions in data_list to create lines between each year's position
        for i in range(len(YEARS) - 1):
            x1 = data_list[i][0]
            y1 = data_list[i][1]
            x2 = data_list[i + 1][0]
            y2 = data_list[i + 1][1]
            line_width = LINE_WIDTH  # Set the width of the line
            line_color = COLORS[color]  # color for the line
            # drawing lines (x1, y1) 和 (x2, y2) 連起來
            canvas.create_line(x1, y1, x2, y2, width=line_width, fill=line_color)

        # Update the color
        color += 1
        if color >= len(COLORS):
            color = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
