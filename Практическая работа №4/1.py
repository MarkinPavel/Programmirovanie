import math

x = float(input("Введите число x: "))

floor_x = math.floor(x)
ceil_x = math.ceil(x)

result = floor_x + ceil_x
print(int(result))