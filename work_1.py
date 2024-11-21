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
        y = self.oval_radius * math.sin(self.angle) + self.win.getHeight()* 3 / 4
        self.circle.move(x - self.circle.getCenter().getX(), y - self.circle.getCenter().getY())
        return x, y
win_width = 1000
win_height = 1000
oval_radius = 200
ball_radius = 10
n_balls = 6
M = 144

win = GraphWin("Balls Moving in an Oval", win_width, win_height)
win.setBackground("black")

balls = []
polygon = Polygon()
polygon.setFill("lightgrey")
polygon.setOutline("red")
polygon.draw(win)

for i in range(n_balls):
    angle = (2 * math.pi / n_balls) * i
    ball = Ball(win, ball_radius, oval_radius, angle)
    balls.append(ball)

target_point = Point(500, 100)
while True:
    points = []
    lines = []
    pl = [target_point]
    pli = []
    i = 0
    m = n_balls/2
    for ball in balls:
        x, y = ball.move()
        pl.append(Point(x, y))
        plii = Polygon(pl)
        plii.setFill("Purple")
        plii.draw(win)
        pli.append(plii)
        if len(pl) == 3:
            pl = [target_point]
        points.append(Point(x, y))
        line = Line(Point(x, y), target_point)
        lines.append(line)
        i+=1
    polygon.undraw()
    polygon = Polygon(*points)
    polygon.setOutline("red")
    #polygon.setFill("Purple")
    polygon.draw(win)
    for line in lines:
        line.setFill("red")
        line.draw(win)
    ball1 = Circle(target_point, 15)
    ball1.setFill("blue")
    ball1.draw(win)
    update(M)
    time.sleep(1/M)
    for line in lines:
        line.undraw()
    for i in pli:
        i.undraw()
