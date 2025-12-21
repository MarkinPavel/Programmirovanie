n = int(input("Введите количество школьников: "))
k = int(input("Введите количество мандаринов: "))

mandarins_per_student = k // n

mandarins_left = k % n

print("Кол-во мандаринов доставшееся каждому школьнику ",mandarins_per_student)
print("Кол-во мандаринов оставшееся в корзине ", mandarins_left)