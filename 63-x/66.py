from graphics import *
import math

def drawNN(win, p1, p2, depth):
    if depth == 0:
        line = Line(p1, p2)
        line.setWidth(2)
        line.draw(win)
        return
    x1 = (2 * p1.x + p2.x) / 3
    y1 = (2 * p1.y + p2.y) / 3
    
    x2 = (p1.x + 2 * p2.x) / 3
    y2 = (p1.y + 2 * p2.y) / 3
    peak_x = (x1 + x2) / 2 + math.sqrt(3) * (y1 - y2) / 2
    peak_y = (y1 + y2) / 2 + math.sqrt(3) * (x2 - x1) / 2
    peak = Point(peak_x, peak_y)
    drawNN(win, p1, Point(x1, y1), depth - 1)
    drawNN(win, Point(x1, y1), peak, depth - 1)
    drawNN(win, peak, Point(x2, y2), depth - 1)
    drawNN(win, Point(x2, y2), p2, depth - 1)

def draw(depth):
    win = GraphWin("Koch", 700, 700)
    win.setBackground("white")
    p1 = Point(300, 100) 
    p2 = Point(100, 500) 
    p3 = Point(500, 500) 
    drawNN(win, p1, p2, depth)
    drawNN(win, p2, p3, depth)
    drawNN(win, p3, p1, depth)

    win.getMouse() 
    win.close() 

for _ in range(10):
    draw(_)

