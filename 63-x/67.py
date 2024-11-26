from graphics import *
import math

def draw_branch(win, start, angle, length, depth):
    if depth == 0:
        return
    end_x = start.x + length * math.cos(angle)
    end_y = start.y - length * math.sin(angle)
    end = Point(end_x, end_y)

    line = Line(start, end)
    line.setWidth(depth/2) 
    line.setOutline("purple")
    line.draw(win)

    new_length = length * 0.7
    draw_branch(win, end, angle - math.radians(30), new_length, depth - 1)  
    draw_branch(win, end, angle + math.radians(30), new_length, depth - 1)  

win = GraphWin("Fractal Nigger", 800, 800)
win.setBackground("white")
start = Point(400, 700)
initial_length = 200 
initial_angle = math.radians(90)  
draw_branch(win, start, initial_angle, initial_length, 14)

win.getMouse()  
win.close() 
