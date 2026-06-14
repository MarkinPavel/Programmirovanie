import random

def filter_positive_elements(nested_list):
    """
    Создаёт новый вложенный список, содержащий только положительные элементы.
    """

    filtered_list = []
    row = 0

    while row < len(nested_list):
        filtered_row = []
        col = 0

        # Фильтруем положительные элементы в строке
        while col < len(nested_list[row]):
            if nested_list[row][col] > 0:  # Только положительные (>0)
                filtered_row.append(nested_list[row][col])
            col += 1

        if filtered_row:
            filtered_list.append(filtered_row)
        else:
            filtered_list.append([])

        row += 1

    return filtered_list

nested_list = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]

print("Исходный список:")
for row in nested_list:
   print(row)

filtered_list = filter_positive_elements(nested_list)

print("\nОтфильтрованный список: ")
for row in filtered_list:
   print(row)