a = int(input("Введите первое число: "))

while True:
    b = int(input("Введите второе число: "))
    if b > a:
        break
    else:
        print("Ошибка. Введите второе число заново")

while True:
    c = int(input("Введите третье число: "))
    if c > b:
        break
    else:
        print("Ошибка. Введите третье число заново")

print("Последовательность принята")