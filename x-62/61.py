from graphics import *
import math
import time

class Clock:
    def __init__(self):
        self.win = GraphWin("Clock", 400, 400)
        self.win.setBackground("white")
        self.center = Point(200, 200)
        self.radius = 150
        
        self.draw_clock_face()
        
        while True:
            self.update_clock()
            time.sleep(1)

    def draw_clock_face(self):
        circle = Circle(self.center, self.radius)
        circle.setOutline("black")
        circle.setWidth(2)
        circle.draw(self.win)

        for hour in range(12):
            angle = math.radians(hour * 30)
            x = self.center.getX() + self.radius * 0.85 * math.cos(angle - math.pi / 2)
            y = self.center.getY() + self.radius * 0.85 * math.sin(angle - math.pi / 2)
            text = Text(Point(x, y), str(hour if hour != 0 else 12))
            text.setSize(14)
            text.draw(self.win)

    def draw_hand(self, angle, length, width, color):
        x_end = self.center.getX() + length * math.cos(angle - math.pi / 2)
        y_end = self.center.getY() + length * math.sin(angle - math.pi / 2)
        line = Line(self.center, Point(x_end, y_end))
        line.setWidth(width)
        line.setFill(color)
        line.draw(self.win)

    def update_clock(self):
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        for item in self.win.items[:]:
            if isinstance(item, Line):
                item.undraw()

        hour_angle = math.radians(hours * 30 + minutes * 0.5)  
        minute_angle = math.radians(minutes * 6)  
        second_angle = math.radians(seconds * 6) 
        self.draw_hand(hour_angle, self.radius * 0.5, 6, "black")
        self.draw_hand(minute_angle, self.radius * 0.75, 4, "black")
        self.draw_hand(second_angle, self.radius * 0.9, 2, "red")

clock = Clock()
