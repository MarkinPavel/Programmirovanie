items = list(map(int, input("Список предметов: ").split()))

ascending = list(items)
i = 0
while i < len(ascending) - 1:
    j = 0
    while j < len(ascending) - 1 - i:
        if ascending[j] > ascending[j + 1]:
            ascending[j], ascending[j + 1] = ascending[j + 1], ascending[j]
        j += 1
    i += 1

descending = list(items)
i = 0
while i < len(descending) - 1:
    j = 0
    while j < len(descending) - 1 - i:
        if descending[j] < descending[j + 1]:
            descending[j], descending[j + 1] = descending[j + 1], descending[j]
        j += 1
    i += 1

reversed_list = []
i = len(items) - 1
while i >= 0:
    reversed_list.append(items[i])
    i -= 1

print(f"Сортировка по возрастанию: {ascending}")
print(f"Сортировка по убыванию: {descending}")
print(f"Просмотр в порядке сбора: {items}")
print(f"Просмотр в обратном порядке: {reversed_list}")