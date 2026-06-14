n = int(input("Ведите кол-во строк: "))

all_chars = []

for i in range(n):

   s = input("Введите символы строки: ")

   all_chars.extend(s)

print(all_chars)
