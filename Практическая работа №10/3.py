# Задача 3. «Рекордсмен»
# Программа находит максимальное число в последовательности

# Переменная для хранения максимума
max_number = 0

while True:
    number = int(input("Введите число: "))

    if number == 0:
        break

    if number > max_number:
        max_number = number

print(max_number)