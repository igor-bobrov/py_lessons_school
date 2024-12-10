from graphics import *
def level(window, ax, ay, bx, by, depth):
    if depth > 0:
        dx,dy = bx-ax, ay-by
        x3,y3 = bx-dy, by-dx
        x4,y4 = ax-dy, ay-dx
        x5,y5 = x4 + (dx - dy)/2, y4 - (dx + dy)/2
        Line(Point(ax, ay), Point(bx, by)).draw(window)
        Line(Point(bx, by), Point(x3, y3)).draw(window)
        Line(Point(x3, y3), Point(x4, y4)).draw(window)
        Line(Point(x4, y4), Point(ax, ay)).draw(window)
        level(window, x4, y4, x5, y5, depth - 1)
        level(window, x5, y5, x3, y3, depth - 1)
win = GraphWin("Koch", 700, 700)
level(win, 300, 600, 400, 600, depth=10)
win.getMouse() 
win.close()