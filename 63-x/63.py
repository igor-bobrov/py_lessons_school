import turtle

def draw_triangle(points):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])

def sierpinski(points, depth):
    if depth == 0:
        draw_triangle(points)
    else:
        mid1 = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
        mid2 = ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
        mid3 = ((points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2)

        sierpinski([points[0], mid1, mid3], depth - 1)
        sierpinski([points[1], mid1, mid2], depth - 1)
        sierpinski([points[2], mid2, mid3], depth - 1)

turtle.speed(100)
turtle.hideturtle()

points = [(-200, -150), (0, 200), (200, -150)]
sierpinski(points, 6)

turtle.done() 
