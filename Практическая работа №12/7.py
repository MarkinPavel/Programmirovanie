numbers = [10, 20, 30, 40, 50]

number = int(input("Введите число: "))

for i in range(len(numbers)):
   if numbers[i] == number:
       break
   if i == len(numbers) - 1:
       print("Нет такого числа")
