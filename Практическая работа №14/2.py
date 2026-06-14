import random

def process_nested_list(nested_list):
    """
    Вычисляет суммы строк, общую сумму и находит строку с максимальной суммой.
    """
    row_sums = []
    total_sum = 0
    max_sum = 0
    max_row_index = -1

    row = 0
    while row < len(nested_list):
        row_sum = 0
        col = 0

        # Суммируем элементы текущей строки
        while col < len(nested_list[row]):
            row_sum += nested_list[row][col]
            col += 1

        row_sums.append(row_sum)
        total_sum += row_sum

        if row_sum > max_sum:
            max_sum = row_sum
            max_row_index = row

        row += 1

    return row_sums, total_sum, max_row_index

nested_list = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

for row in nested_list:
   print(row)

result = process_nested_list(nested_list)

print(f"\nСуммы строк: {result[0]}")
print(f"Общая сумма всех элементов: {result[1]}")
print(f"Строка с максимальной суммой: {result[2]} ({result[0][result[2]]})")