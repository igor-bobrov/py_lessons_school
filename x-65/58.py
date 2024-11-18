from graphics import *
import time

class Ball:
    def __init__(self, win, radius, color, dx, dy, x, y):
        self.win = win
        self.radius = radius
        self.color = color
        self.circle = Circle(Point(x, y), radius)
        self.circle.setFill(color)
        self.circle.draw(win)
        self.dx, self.dy = dx, dy

    def move(self):
        self.circle.move(self.dx + border1.dx, self.dy + border1.dy)
        if self.circle.getCenter().getX() <= self.radius + border1.x or self.circle.getCenter().getX() >= self.win.getWidth() - self.radius - 2*border1.x:
            self.dx = abs(self.dx)
        if self.circle.getCenter().getY() <= self.radius + border1.y or self.circle.getCenter().getY() >= self.win.getHeight() - self.radius - 2*border1.y:
            self.dy = abs(self.dy)


    def check_collision(self, other_ball):
        dist = ((self.circle.getCenter().getX() - other_ball.circle.getCenter().getX()) ** 2 +
                 (self.circle.getCenter().getY() - other_ball.circle.getCenter().getY()) ** 2) ** 0.5
        return dist <= (self.radius + other_ball.radius)

class Border:
    def __init__(self, win, x, y, dx, dy, color):
        self.win = win
        self.x = x
        self.y = y
        self.color = color
        self.rectangle = Rectangle(Point(x, y), Point(win_width - x, win_height - y))
        self.rectangle.setOutline(color)
        self.rectangle.draw(win)
        self.dx, self.dy = dx, dy
    def move(self):
        self.rectangle.move(self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        if self.x == 0 or self.x == 100:
            self.dx = -self.dx  
        if self.y == 0 or self.y == 100:
            self.dy = -self.dy

win_width = 1200
win_height = 800
win = GraphWin("Drag Balls", win_width, win_height)
ball1 = Ball(win, 20, "red", 3, 3, 90, 90)
ball2 = Ball(win, 30, "blue", -3, -3, 300, 300)
border1 = Border(win, 50, 50, 1, 2, "blue")

while True:
    border1.move()
    ball1.move()
    ball2.move()
    if ball1.check_collision(ball2):
        ball1.dx = -ball1.dx
        ball1.dy = -ball1.dy
        ball2.dx = -ball2.dx
        ball2.dy = -ball2.dy

    time.sleep(0.02)

    if win.checkMouse():
        break

win.close()

