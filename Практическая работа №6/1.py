temperature = int(input("Введите свою температуру: "))
pressure = int(input("Введите своё давление: "))
pulse = int(input("Введите свой пульс: "))

if (temperature < 35 or temperature > 38 or
    pressure < 105 or pressure > 140 or
    pulse < 55 or pulse > 110):
    print("Требуется врач")

elif (36 <= temperature <= 37 and
      110 <= pressure <= 130 and
      60 <= pulse <= 100):
    print("Нормальное состояние здоровья")

else:
    print("Лёгкое недомогание")