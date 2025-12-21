pocket = int(input("Введите номер кармана: "))

if pocket == 0:
    print("карман зелёного цвета")

elif (1 <= pocket <= 10):
    if (pocket % 2 == 0):
        print("Карман чёрного цвета")
    else:
        print("Карман красного цвета")

elif (11 <= pocket <= 18):
    if (pocket % 2 == 0):
        print("Карман красного цвета")
    else:
        print("Карман чёрного цвета")

elif (19 <= pocket <= 28):
    if (pocket % 2 == 0):
        print("Карман чёрного цвета")
    else:
        print("Карман красного цвета")

elif (29 <= pocket <= 36):
    if (pocket % 2 == 0):
        print("Карман красного цвета")
    else:
        print("Карман чёрного цвета")
elif(pocket > 36 or pocket < 0):
    print("Число находится вне диапазон")