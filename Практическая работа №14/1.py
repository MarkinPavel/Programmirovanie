import random


def find_max_element(nested_list):
   """
   Находит максимальный элемент во вложенном списке и возвращает его позицию.
   """
   max_value = nested_list[0][0]
   max_row = 0
   max_col = 0
   row = 0


   while row < len(nested_list):
       col = 0
       while col < len(nested_list[row]):
           if nested_list[row][col] > max_value:
               max_value = nested_list[row][col]
               max_row = row
               max_col = col
           col += 1
       row += 1


   return (max_row, max_col)

nested_list = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
for row in nested_list:
   print(row)


# Поиск максимального элемента
max_position = find_max_element(nested_list)
print(f"\nМаксимальный элемент: строка {max_position[0]}, позиция {max_position[1]}")
print(f"Значение максимального элемента: {nested_list[max_position[0]][max_position[1]]}")
