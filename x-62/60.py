from graphics import *
import math
import time

win = GraphWin("piramida", 1000, 1000, autoflush=False)
high = Circle(Point(500, 100), 20)
high.setFill("red")
high.draw(win)

planet_radius = 100
moon_radius = 20

win.setBackground("black")

while True:
    planet_angle = (time.time() % (2 * math.pi)) / (2 * math.pi) * (2 * math.pi)
    planet_x = 400 + planet_radius * math.cos(planet_angle)
    planet_y = 400 + planet_radius * math.sin(planet_angle)

    planet = Circle(Point(planet_x, planet_y), 10)
    planet.setFill("blue")
    planet.draw(win)

    update(60)
    time.sleep(1/60)
    planet.undraw()
    
    
    if win.checkMouse(): 
        break

win.close()               
