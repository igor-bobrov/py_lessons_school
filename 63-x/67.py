import turtle
import math

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def pythagorean_tree(t, size, level):
    if level == 0:
        return

    draw_square(t, size)

    t.forward(size)
    t.left(90)

    pythagorean_tree(t, size / math.sqrt(2), level - 1)

    t.right(90)
    t.forward(size / math.sqrt(2))
    t.right(90)
    
    pythagorean_tree(t, size / math.sqrt(2), level - 1)

    t.left(90)
    t.backward(size / math.sqrt(2))
    t.left(90)
    t.backward(size)
    t.right(90)

screen = turtle.Screen()
screen.title("Квадратное дерево Пифагора")
t = turtle.Turtle()
t.speed(0)  
t.penup()
t.goto(-200, -200)
t.pendown()

pythagorean_tree(t, 200, 5) 

t.hideturtle()
screen.mainloop()
