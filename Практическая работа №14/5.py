def max_loot_value(n, items):
    """
    Находит максимальную суммарную ценность N предметов.
    """
    # Сортировка предметов по убыванию ценности
    i = 0
    while i < len(items) - 1:
        j = i + 1
        while j < len(items):
            if items[i] < items[j]:
                # Меняем местами
                items[i], items[j] = items[j], items[i]
            j += 1
        i += 1

    # Берём N самых ценных предметов
    total = 0
    i = 0
    while i < n and i < len(items):
        total += items[i]
        i += 1

    return total


n = int(input("Сколько предметов может унести игрок: "))
items = list(map(int, input("Ценности предметов: ").split()))

result = max_loot_value(n, items)

print(f"\nМаксимальная суммарная ценность: {result}")