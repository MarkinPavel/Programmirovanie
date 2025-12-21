print("Калькулятор ИМТ\n")

data = input("Введите ваш вес(кг) и рост(м): ")

values = data.split()

weight = values[0].replace(",", ".")
height = values[1].replace(",", ".")

weight = float(weight)
height = float(height)

bmi = weight / (height * height)

print(f"\n Ваш индекс массы тела: {bmi:.1f}\n")