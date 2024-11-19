from graphics import *
import time
import numpy as np
M = 3
N = 5
Width = 800
Height = 800
R = 200
radian = (np.pi*(M-2)/M)/2
newR = R/np.sin(radian)
X1 = np.linspace(0, 2*np.pi, N+1)
X2 = np.linspace(0, 2*np.pi, M+1)
def outputpoint(X, r):
    pointer = []
    for el in X:
        x = Width/2 + r - r*(1 - np.cos(el))
        y = Height/2 + r - r*(1 - np.sin(el))
        lists = [float(x),float(y)]
        pointer.append(lists)
    return pointer
Print1 = outputpoint(X1, R)
Print2 = outputpoint(X2, newR)
def gr():
    win = GraphWin('фигуры', Width, Height)
    c = Circle(Point(Width/2,Height/2), R)
    c.setFill('gray')
    c.draw(win)
    for i in range(len(Print1)-1):
        v = Line(Point(Print1[i][0], Print1[i][1]), Point(Print1[i+1][0], Print1[i+1][1]))
        v.setOutline('black')
        v.draw(win)
    for i in range(len(Print2)-1):
        b = Line(Point(Print2[i][0], Print2[i][1]), Point(Print2[i+1][0], Print2[i+1][1]))
        b.setOutline('black')
        b.draw(win)
    time.sleep(5)
gr()