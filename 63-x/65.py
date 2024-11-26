from graphics import *
import math

def draw_branch(win, start, angle, length, depth, n):
    if depth == 0:
        return

    end_x = start.x + length * math.cos(math.radians(angle))
    end_y = start.y - length * math.sin(math.radians(angle))
    end_point = Point(end_x, end_y)

    line = Line(start, end_point)
    line.setWidth(2)
    line.draw(win)
    new_length = length / 3
    for i in range(n):
        new_angle = angle - (180 / n) * (i - n // 2) 
        draw_branch(win, end_point, new_angle, new_length, depth - 1, n)

def draw_snowflake(n, depth):
    win = GraphWin(f"Snowflake (n={n})", 600, 600)
    center = Point(300, 300)

    length = 200
    for i in range(n):
        angle = 360 / n * i
        draw_branch(win, center, angle, length, depth, n)

    win.getMouse()  
    win.close()  

for n in [4, 3, 6]:
    draw_snowflake(n, depth=4) 

