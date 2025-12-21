num1 = input("Введите первое число ")
num2 = input("Ввеедите второе число ")

try:
    num1 = int(num1)
    num2 = int(num2)

    num3 = num1 + num2
    print(num3)

except:
    print("Ошибка, невозможно сложить буквы")