from graphics import *
import math
import time

class Ball:
    def __init__(self, win, radius, oval_radius, angle):
        self.win = win
        self.radius = radius
        self.oval_radius = oval_radius
        self.angle = angle
        self.circle = Circle(Point(oval_radius * math.cos(angle) + win.getWidth() / 2,
                                   oval_radius * math.sin(angle) + win.getHeight() / 2),
                             radius)
        self.circle.setFill("blue")
        self.circle.draw(win)

    def move(self):
        self.angle += 0.05 
        if self.angle >= 2 * math.pi:
            self.angle -= 2 * math.pi
        x = 2*self.oval_radius * math.cos(self.angle) + self.win.getWidth() / 2
        y = self.oval_radius * math.sin(self.angle) + self.win.getHeight() *2 / 3
        self.circle.move(x - self.circle.getCenter().getX(), y - self.circle.getCenter().getY())
        return x, y
win_width = 1000
win_height = 1000
oval_radius = 200  
ball_radius = 10   
n_balls = 12

win = GraphWin("Balls Moving in an Oval", win_width, win_height)
win.setBackground("black")
balls = []
for i in range(n_balls):
    angle = (2 * math.pi / n_balls) * i 
    balls.append(Ball(win, ball_radius, oval_radius, angle))
high = Circle(Point(win_width/2, 100), ball_radius)
high.setFill("blue")
high.draw(win)
polygon = Polygon()
polygon.setOutline("red")
polygon.draw(win)
lines = []
for i in range(n_balls):
    lines.append(Line([Point(win_width/2, 100), Point(win_width/2, 100)]))
while True:
    points = []
    for i in range(n_balls):
        x, y = balls[i].move()
        points.append(Point(x, y))

    polygon.undraw()
    polygon = Polygon(*points)
    polygon.setOutline("red")
    polygon.draw(win)
    time.sleep(1/30)
    update(60)
    if win.checkMouse(): break