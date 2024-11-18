from graphics import *
import math
import time

def draw_circle_points(radius, num_points):
    win = GraphWin("Circle Points", 400, 400)
    center = Point(200, 200)

    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = center.x + radius * math.cos(angle)
        y = center.y + radius * math.sin(angle)
        point = Point(x, y)
        point.draw(win)

    win.getMouse()
    win.close()

def draw_spiral(num_points):
    win = GraphWin("Spiral", 400, 400)
    center = Point(200, 200)
    angle_increment = 0.1
    radius_increment = 2

    for i in range(num_points):
        angle = angle_increment * i
        radius = radius_increment * i
        x = center.x + radius * math.cos(angle)
        y = center.y + radius * math.sin(angle)
        point = Point(x, y)
        point.draw(win)

    win.getMouse()
    win.close()

def draw_circles(radius, num_circles):
    win = GraphWin("Circles", 400, 400)
    center = Point(200, 200)

    for i in range(num_circles):
        if i > 0:
            prev_circle.undraw()  
        circle = Circle(center, radius * (i + 1))
        circle.draw(win)
        prev_circle = circle
        time.sleep(0.5)  

    win.getMouse()
    win.close()

def draw_planets_with_moons():
    win = GraphWin("Planets and Moons", 800, 800, autoflush=False)
    sun = Circle(Point(400, 400), 30)
    sun.setFill("yellow")
    sun.draw(win)

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

        moon_angle = 12* (time.time() % (2 * math.pi)) / (2 * math.pi) * (2 * math.pi) + (2 * math.pi)
        moon_x = planet_x + moon_radius * math.cos(moon_angle)
        moon_y = planet_y + moon_radius * math.sin(moon_angle)

        moon = Circle(Point(moon_x, moon_y), 3) 
        moon.setFill("gray")
        moon.draw(win)
        update(60)
        time.sleep(1/60)
        planet.undraw()
        moon.undraw()
        
        if win.checkMouse(): 
            break

    win.close()

draw_circle_points(100, 12)  
draw_spiral(100)               
draw_planets_with_moons()     
