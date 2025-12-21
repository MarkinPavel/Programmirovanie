import math

x = float(input("Введите число x: "))
x_rad = math.radians(x)

result = math.sin(x_rad) + math.cos(x_rad) + (math.tan(x_rad) ** 2)
print(result)