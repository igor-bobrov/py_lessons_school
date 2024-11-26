from graphics import *

def draw_sierpinski_square(win, top_left, size, depth):
    if depth == 0:
        square = Rectangle(top_left, Point(top_left.x + size, top_left.y + size))
        square.setFill("black")
        square.draw(win)
    else:
        new_size = size / 2
        draw_sierpinski_square(win, top_left, new_size, depth - 1)
        draw_sierpinski_square(win, Point(top_left.x + new_size, top_left.y), new_size, depth - 1)
        draw_sierpinski_square(win, Point(top_left.x, top_left.y + new_size), new_size, depth - 1)
        draw_sierpinski_square(win, Point(top_left.x + new_size, top_left.y + new_size), new_size, depth - 1)

win = GraphWin("Sierpinski", 600, 600)
depth = 6
size = 300  
top_left = Point(150, 150) 
draw_sierpinski_square(win, top_left, size, depth)

win.getMouse()
win.close() 
