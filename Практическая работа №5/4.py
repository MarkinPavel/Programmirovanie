import math

def calculate_recangle_area(width, height):
    """
    Вычислает площадь прямоугольника.

    Параметры:
    widht (float): ширина прямоугольника
    height (float): высота прямоугольника

    Возвращает:
    float: площадь прямоугольника (ширина * высота)
    """
    return width * height

def calculate_circle_area(radius):
    """
    Вычисляет площадь круга.

    Параметры:
    radius (float): радиус круга

    Возвращает:
    float: площадь круга (pi * радиус)
    """
    return math.pi * (radius ** 2)

print("Калькулятор площади\n")

rectangle_width = float(input("Введите ширину прямоугольника: "))
rectangle_height = float(input("Введите высоту прямоугольника: "))
circle_radius = float(input("Введите радиус круга: "))

rectangle_area = calculate_recangle_area(rectangle_width, rectangle_height)
circle_area = calculate_circle_area(circle_radius)

print(f"Площадь прямоугольника: {rectangle_area:.2f}")
print(f"Площадь круга: {circle_area:.2f}")

