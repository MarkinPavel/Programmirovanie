def print_labyrinth(labyrinth_string):
    """
    Задание 1.1: Вывод лабиринта в виде сетки 5x5
    """
    print("\nЛабиринт (5x5):")
    for i in range(0, 25, 5):
        print(labyrinth_string[i:i+5])

def find_position(labyrinth_string, symbol):
    """
    Вспомогательная функция для поиска координат символа в лабиринте
    """
    index = labyrinth_string.find(symbol)
    if index == -1:
        return None
    row = index // 5
    col = index % 5
    return row, col


labyrinth_input = input("Введите строку из 25 символов, представляющую лабиринт: ")

while len(labyrinth_input) != 25:
    print("Ошибка: строка должна содержать ровно 25 символов!")
    labyrinth_input = input("Введите строку из 25 символов, представляющую лабиринт: ")

# Задание 1.1 Вывести лабиринт
print_labyrinth(labyrinth_input)

# Задание 1.2: Определить координату входа в лабиринт
entrance_pos = find_position(labyrinth_input, 'н')
if entrance_pos:
    entrance_row, entrance_col = entrance_pos
    print(f"\nКоординаты входа (н): строка {entrance_row}, столбец {entrance_col}")
else:
    print("\nВход (н) не найден в лабиринте!")
    exit()

# Задание 1.3: Определить координату выхода из лабиринта
exit_pos = find_position(labyrinth_input, 'ф')
if exit_pos:
    exit_row, exit_col = exit_pos
    print(f"Координаты выхода (ф): строка {exit_row}, столбец {exit_col}")
else:
    print("Выход (ф) не найден в лабиринте!")
    exit()  # Завершаем программу, если выход не найден

# Задание 1.4: Определить расстояние между входом и выходом в шагахz
manhattan_distance = abs(entrance_row - exit_row) + abs(entrance_col - exit_col)
print(f"Манхэттенское расстояние между входом и выходом: {manhattan_distance} шагов")

# Задание 1.5: Подсчитать, сколько монет можно собрать в лабиринте
coin_count = labyrinth_input.count('м')

coins_display = '🟡' * coin_count
print(f"\nКоличество монет в лабиринте: {coin_count}")
print(f"Монеты: {coins_display if coin_count > 0 else 'Нет монет'}")

# Задание 1.6: Подсчитать сколько здоровья останется после встречи со всеми ловушками и врагами
initial_hp = 100
trap_count = labyrinth_input.count('л')
enemy_count = labyrinth_input.count('з')

total_damage = trap_count * 10 + enemy_count * 50
remaining_hp = max(0, initial_hp - total_damage)

full_hearts = remaining_hp // 10
empty_hearts = (initial_hp - remaining_hp) // 10

hearts_display = '♥' * full_hearts + '♡' * empty_hearts

print(f"\nСтатистика здоровья:")
print(f"Ловушек: {trap_count} (-{trap_count * 10} HP)")
print(f"Врагов: {enemy_count} (-{enemy_count * 50} HP)")
print(f"Общий урон: -{total_damage} HP")
print(f"Оставшееся здоровье: {remaining_hp} HP")
print(f"Индикатор здоровья: {hearts_display}")

# Задание 1.7: Заменить символы лабиринта на эмодзи
emoji_map = {
    '0': '⬜',  # проход
    '1': '⬛',  # стена
    'л': '🔷',  # словушка
    'м': '🟡',  # монета
    'ф': '🟫',  # выход
    'з': '🐷',  # враг
    'н': '⭐'   # вход
}

emoji_labyrinth = ''.join(emoji_map.get(char, char) for char in labyrinth_input)

print("\nЛабиринт с эмодзи:")
for i in range(0, 25, 5):
    print(emoji_labyrinth[i:i + 5])