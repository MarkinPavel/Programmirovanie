ipaddress = input("Введите ip адрес: ")

parts = ipaddress.split(".")

for i in parts:
   if int(i) < 0 or int(i) > 255:
       print("НЕТ")
       exit()

print("ДА")
