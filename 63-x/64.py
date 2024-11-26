from graphics import *

def draw_sierpinski_square(win, top_left, size, depth):
    if depth == 0:
        square = Rectangle(top_left, Point(top_left.x + size, top_left.y + size))
        square.setFill("black")
        square.draw(win)
    else:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue 
                draw_sierpinski_square(win,
                                        Point(top_left.x + i * new_size, top_left.y + j * new_size),
                                        new_size,
                                        depth - 1)

win = GraphWin("Nigger Square", 600, 600)
win.setBackground("white")
draw_sierpinski_square(win, Point(100, 100), 400, 4) 

win.getMouse() 
win.close() 

