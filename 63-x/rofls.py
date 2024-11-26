import pygame
import math

# Настройки
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Fractal Tree")

def draw_branch(surface, start, angle, length, depth):
    if depth == 0:
        return

    # Вычисляем конечную точку ветви
    end_x = start[0] + length * math.cos(angle)
    end_y = start[1] - length * math.sin(angle)
    end = (end_x, end_y)

    # Рисуем ветвь
    pygame.draw.line(surface, LINE_COLOR, start, end, width=depth)

    # Рекурсивно рисуем две новые ветви
    new_length = length * 0.7  # Уменьшаем длину ветвей
    draw_branch(surface, end, angle - math.radians(30), new_length, depth - 1)  # Левая ветвь
    draw_branch(surface, end, angle + math.radians(30), new_length, depth - 1)  # Правая ветвь

clock = pygame.time.Clock()
depth = 5  # Начальная глубина рекурсии

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Увеличить глубину
                depth += 1
            elif event.key == pygame.K_DOWN:  # Уменьшить глубину
                depth = max(0, depth - 1)

    # Отрисовка
    screen.fill(BACKGROUND_COLOR)
    start = (WIDTH // 2, HEIGHT)  # Начальная точка (основание дерева)
    initial_length = 100  # Начальная длина ветви
    initial_angle = math.radians(90)  # Начальный угол (90 градусов)

    draw_branch(screen, start, initial_angle, initial_length, depth)

    pygame.display.flip()  # Обновляем экран
    clock.tick(60)  # Ограничиваем до 60 кадров в секунду

pygame.quit()

