import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = float(input("Введите координаты точки x1: "))
y1 = float(input("Введите координаты точки y1: "))
x2 = float(input("Введите координаты точки x2: "))
y2 = float(input("Введите координаты точки y2: "))

result = calculate_distance(x1, y1, x2, y2)
print(f"Расстояние между точками: {result:.2f}")