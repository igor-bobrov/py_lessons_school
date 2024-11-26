from graphics import *
import math

def draw_snowflake(win, center, length, depth, branches):
    if depth == 0:
        return
    angles = [2 * math.pi * i / branches for i in range(branches)]

    for i in range(len(angles)):
        end_x = center.x + length * math.cos(angles[i])
        end_y = center.y + length * math.sin(angles[i])
        end = Point(end_x, end_y)

        line = Line(center, end)
        line.setWidth(depth)  
        line.draw(win)

        draw_snowflake(win, end, length / 3, depth - 1, branches)

n_values = [3, 4, 6]
length = 200 

for n in n_values:
    win = GraphWin(f"Snowflake (n={n})", 600, 600)
    win.setBackground("white")

    center = Point(300, 300)  
    draw_snowflake(win, center, length, 6, n) 

    win.getMouse() 
    win.close() 

