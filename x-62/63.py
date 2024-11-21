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
        # Обновляем угол для движения по овалу
        self.angle += 0.05  # Скорость движения
        if self.angle >= 2 * math.pi:  # Сброс угла после полного оборота
            self.angle -= 2 * math.pi
        
        # Обновляем координаты шарика
        x = self.oval_radius * math.cos(self.angle) + self.win.getWidth() / 2
        y = self.oval_radius * math.sin(self.angle) + self.win.getHeight() / 2
        self.circle.move(x - self.circle.getCenter().getX(), y - self.circle.getCenter().getY())
        return x, y  # Возвращаем текущие координаты

def main():
    win_width = 800
    win_height = 600
    oval_radius = 200  # Радиус овала
    ball_radius = 10   # Радиус шарика
    n_balls = 5        # Количество шариков

    win = GraphWin("Balls Moving in an Oval", win_width, win_height)
    win.setBackground("white")

    # Создаем n шариков с равномерным распределением по овалу
    balls = []
    polygon = Polygon()  # Создаем многоугольник
    polygon.setFill("lightgrey")
    polygon.setOutline("red")
    polygon.draw(win)

    for i in range(n_balls):
        angle = (2 * math.pi / n_balls) * i  # Начальный угол для каждого шарика
        ball = Ball(win, ball_radius, oval_radius, angle)
        balls.append(ball)

    # Основной цикл движения шариков
    while True:
        points = []  # Список для хранения точек многоугольника

        for ball in balls:
            x, y = ball.move()
            points.append(Point(x, y))  # Добавляем текущие координаты шарика в список точек

        # Обновляем многоугольник
        polygon.undraw()  # Убираем старый многоугольник
        polygon = Polygon(*points)  # Создаем новый многоугольник из текущих точек
        polygon.setFill("lightgrey")
        polygon.setOutline("red")
        polygon.draw(win)  # Рисуем новый многоугольник

        time.sleep(0.05)  # Задержка для управления скоростью

if __name__ == "__main__":
    main()
