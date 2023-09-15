"""
File: my_drawing
Name: 皓暄
----------------------
TODO: Practice with GPolygon, fill_color, GOval, GArc, GLabel, .font, ect.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: GPolygon Bird
    """
    window = GWindow(width=800, height=400, title='window')
    for i in range(0, window.width, 50):
        for j in range(0, window.height, 50):
            arc2 = GArc(50, 100, 0, 180)
            arc2.color = "silver"
            window.add(arc2, i, j)

    tr01 = GPolygon()
    tr01.add_vertex((250, 100))
    tr01.add_vertex((300, 100))
    tr01.add_vertex((350, 130))
    window.add(tr01)
    tr01.fill_color = "orange"

    tr02 = GPolygon()
    tr02.add_vertex((250, 100))
    tr02.add_vertex((300, 130))
    tr02.add_vertex((350, 130))
    window.add(tr02)
    tr02.fill_color = "orange"

    tr03 = GPolygon()
    tr03.add_vertex((300, 100))
    tr03.add_vertex((350, 90))
    tr03.add_vertex((400, 100))
    tr03.add_vertex((350, 105))
    window.add(tr03)
    tr03.fill_color = "cadetblue"

    tr15 = GPolygon()
    tr15.add_vertex((350, 300))
    tr15.add_vertex((430, 180))
    tr15.add_vertex((380, 180))
    window.add(tr15)
    tr15.fill_color = 'blue'

    tr05 = GPolygon()
    tr05.add_vertex((300, 100))
    tr05.add_vertex((350, 130))
    tr05.add_vertex((400, 100))
    window.add(tr05)
    tr05.fill_color = "cyan"

    tr04 = GOval(15, 15)
    window.add(tr04, x=350, y=107)
    tr04.fill_color = "black"

    tr06 = GPolygon()
    tr06.add_vertex((400, 100))
    tr06.add_vertex((300, 200))
    tr06.add_vertex((350, 300))
    window.add(tr06)
    tr06.fill_color = 'skyblue'

    tr07 = GPolygon()
    tr07.add_vertex((300, 200))
    tr07.add_vertex((350, 130))
    tr07.add_vertex((400, 100))
    window.add(tr07)
    tr07.fill_color = 'deepskyblue'

    tr08 = GPolygon()
    tr08.add_vertex((300, 200))
    tr08.add_vertex((450, 150))
    tr08.add_vertex((430, 180))
    window.add(tr08)
    tr08.fill_color = 'royalblue'

    tr09 = GPolygon()
    tr09.add_vertex((430, 180))
    tr09.add_vertex((350, 300))
    tr09.add_vertex((500, 300))
    window.add(tr09)
    tr09.fill_color = 'steelblue'

    tr11 = GPolygon()
    tr11.add_vertex((350, 300))
    tr11.add_vertex((400, 300))
    tr11.add_vertex((430, 180))
    window.add(tr11)
    tr11.fill_color = 'darkblue'

    tr12 = GPolygon()
    tr12.add_vertex((350, 300))
    tr12.add_vertex((500, 150))
    tr12.add_vertex((430, 180))
    window.add(tr12)
    tr12.fill_color = "navy"

    tr10 = GPolygon()
    tr10.add_vertex((300, 200))
    tr10.add_vertex((400, 250))
    tr10.add_vertex((430, 250))
    window.add(tr10)
    tr10.fill_color = 'blue'

    arc1 = GArc(100, 200, 0, 180)
    arc1.filled = True
    arc1.fill_color = 'tomato'
    arc1.color = "tomato"
    window.add(arc1, x=100, y=150)

    word = GLabel("Hi, I'm GPolygon Bird ☺")
    word.font = 'Verdana-13-bold'
    window.add(word, x=500, y=150)














if __name__ == '__main__':
    main()
