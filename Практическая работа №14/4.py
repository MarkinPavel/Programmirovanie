import random


def find_all_positions(nested_list, search_value):
    """
    Находит все позиции искомого элемента во вложенном списке.
    """
    positions = []

    row = 0
    while row < len(nested_list):
        col = 0
        while col < len(nested_list[row]):
            if nested_list[row][col] == search_value:
                positions.append((row, col))
            col += 1
        row += 1

    return positions

nested_list = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

search_value = random.randint(0, 10)  # Можно заменить на конкретное число, например 5

for row in nested_list:
   print(row)

print(f"\nЗначение для поиска: {search_value}")

positions = find_all_positions(nested_list, search_value)

if positions:
    print(f"\nЗначение {search_value} найден в следующих позициях:")
    for pos in positions:
        print(f"  Строка {pos[0]}, столбец {pos[1]} (значение: {nested_list[pos[0]][pos[1]]})")else:
    print(f"\nЭлемент {search_value} не найден в списке.")