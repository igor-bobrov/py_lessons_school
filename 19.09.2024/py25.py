def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def is_point_inside_triangle(triangle, point):
    x1, y1, x2, y2, x3, y3 = triangle
    x, y = point
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    return A == A1 + A2 + A3
with open('input.txt', 'r') as f:
    x1, y1 = map(int, f.readline().strip().split())
    x2, y2 = map(int, f.readline().strip().split())
    x3, y3 = map(int, f.readline().strip().split())
    x, y = map(int, f.readline().strip().split())

triangle = (x1, y1, x2, y2, x3, y3)
point = (x, y)

if is_point_inside_triangle(triangle, point):
    result = "in"
else:
    result = "out"

with open('output.txt', 'w') as f:
    f.write(f"Dot ({x}, {y}) {result}.\n")
