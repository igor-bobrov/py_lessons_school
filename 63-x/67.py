from graphics import *
import math

def draw_branch(win, start, angle, length, depth):
    if depth == 0:
        return

    # Вычисляем координаты конца ветки
    end_x = start.x + length * math.cos(angle)
    end_y = start.y - length * math.sin(angle)
    end = Point(end_x, end_y)

    # Рисуем ветку
    line = Line(start, end)
    line.setWidth(depth)  # Уменьшаем ширину ветки по мере углубления
    line.draw(win)

    # Рекурсивно рисуем ветви
    new_length = length * 0.7  # Уменьшаем длину ветвей
    draw_branch(win, end, angle - math.pi / 6, new_length, depth - 1)  # Левая ветка
    draw_branch(win, end, angle + math.pi / 6, new_length, depth - 1)  # Правая ветка

def draw_fractal_tree(depth):
    win = GraphWin("Fractal Tree", 600, 600)
    win.setBackground("white")

    # Начальная точка и угол
    start = Point(300, 550)  # Начинаем снизу по центру
    angle = -math.pi / 2  # Угол вверх (90 градусов)
    length = 100  # Длина начальной ветки

    draw_branch(win, start, angle, length, depth)

    win.getMouse()  # Ждем клика мыши
    win.close()  # Закрываем окно

def main():
    depth = 5 
    draw_fractal_tree(depth)

if __name__ == "__main__":
    main()
