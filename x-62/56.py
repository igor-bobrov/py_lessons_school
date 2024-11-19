from graphics import *
import math

def draw_triangle(win, p1, p2, p3):
    triangle = Polygon(p1, p2, p3)
    triangle.setOutline("black")
    triangle.setFill("lightgrey")
    triangle.draw(win)

def draw_circumcircle(win, p1, p2, p3):
    D = 2 * (p1.getX() * (p2.getY() - p3.getY()) +
             p2.getX() * (p3.getY() - p1.getY()) +
             p3.getX() * (p1.getY() - p2.getY()))
    
    if D == 0:
        return
    
    A = p1.getX()**2 + p1.getY()**2
    B = p2.getX()**2 + p2.getY()**2
    C = p3.getX()**2 + p3.getY()**2
    
    center_x = (A * (p2.getY() - p3.getY()) +
                 B * (p3.getY() - p1.getY()) +
                 C * (p1.getY() - p2.getY())) / D
    
    center_y = (A * (p3.getX() - p2.getX()) +
                 B * (p1.getX() - p3.getX()) +
                 C * (p2.getX() - p1.getX())) / D
    
    center = Point(center_x, center_y)
    radius = math.sqrt((center_x - p1.getX())**2 + (center_y - p1.getY())**2)
    
    circumcircle = Circle(center, radius)
    circumcircle.setOutline("blue")
    circumcircle.draw(win)

def draw_incircle(win, p1, p2, p3):
    a = math.sqrt((p2.getX() - p3.getX())**2 + (p2.getY() - p3.getY())**2)
    b = math.sqrt((p1.getX() - p3.getX())**2 + (p1.getY() - p3.getY())**2)
    c = math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    s = (a + b + c) / 2
    radius = math.sqrt((s - a) * (s - b) * (s - c) / s)
    center_x = (a * p1.getX() + b * p2.getX() + c * p3.getX()) / (a + b + c)
    center_y = (a * p1.getY() + b * p2.getY() + c * p3.getY()) / (a + b + c)

    center = Point(center_x, center_y)

    incircle = Circle(center, radius)
    incircle.setOutline("red")
    incircle.draw(win)

win = GraphWin("", 600, 600)

p1 = Point(200, 100)
p2 = Point(100, 400)
p3 = Point(400, 300)

draw_triangle(win, p1, p2, p3)
draw_circumcircle(win, p1, p2, p3)
draw_incircle(win, p1, p2, p3)

win.getMouse()
win.close()