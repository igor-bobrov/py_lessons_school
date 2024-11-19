from graphics import *
import time

WIDTH = 800
HEIGHT = 600
win = GraphWin("Moving Balls", WIDTH, HEIGHT, autoflush=False)

class Ball:
    def __init__(self, win, radius, color, dx, dy, x, y, border_coor, dx_bor, dy_bor):
        self.win = win
        self.radius = radius
        self.color = color
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.border_coor = border_coor
        self.dx_bor = dx_bor
        self.dy_bor = dy_bor
        self.border =  Rectangle(Point(border_coor[0][0], border_coor[0][1]), Point(border_coor[1][0], border_coor[1][1]))
        self.border.draw(win)
        self.circle = Circle(Point(x, y), radius)
        self.circle.setFill(self.color)
        self.circle.draw(win)
    
    def border_move(self):
        self.border.undraw()
        self.border_coor[0][0] += self.dx_bor; self.border_coor[1][0] += self.dx_bor; self.border_coor[0][1] += self.dy_bor; self.border_coor[1][1] += self.dy_bor
        self.border = Rectangle(Point(border_coor[0][0], border_coor[0][1]), Point(border_coor[1][0], border_coor[1][1]))
        self.border.draw(win)

    def circle_move(self):
        self.circle.undraw()
        self.x += self.dx; self.y += self.dy
        self.circle = Circle(Point(self.x, self.y), self.radius)
        self.circle.setFill(self.color)
        self.circle.draw(win)

    def move(self):
        Ball.border_move(self)
        Ball.circle_move(self)
        if self.border_coor[0][0] <= 0 or self.border_coor[1][0] >= WIDTH:
            self.dx_bor = -self.dx_bor
        if self.border_coor[0][1] <= 0 or self.border_coor[1][1] >= HEIGHT:
            self.dy_bor = -self.dy_bor
        
        if self.circle.getCenter().getX() <= self.radius + self.border_coor[0][0] or self.circle.getCenter().getX() >= self.border_coor[1][0] - self.radius:
            self.dx = -self.dx 
            Ball.circle_move(self)

        if self.circle.getCenter().getY() <= self.radius + self.border_coor[0][1] or self.circle.getCenter().getY() >= self.border_coor[1][1] - self.radius:
            self.dy = -self.dy 
            Ball.circle_move(self)

    def check_collision(self, other_ball):
        dist = ((self.circle.getCenter().getX() - other_ball.circle.getCenter().getX())**2 +(self.circle.getCenter().getY() - other_ball.circle.getCenter().getY())**2)**0.5
        return dist <= (self.radius + other_ball.radius)

border_coor =([50, 50], [WIDTH-50, HEIGHT - 50])
dx_bor = 0.5
dy_bor = 0.2

ball1 = Ball(win, 20, "blue", 3, 10, 90, 90, border_coor, dx_bor, dy_bor)
ball2 = Ball(win, 30, "red", -2, -2, 300, 300, border_coor, dx_bor, dy_bor)

while True:
    ball1.move()
    ball2.move()

    if ball1.check_collision(ball2):
        ball1.dx = -ball1.dx
        ball1.dy = -ball1.dy
        ball2.dx = -ball2.dx
        ball2.dy = -ball2.dy
    
    time.sleep(1/60)
    update(60)
    if win.checkMouse():
        break
