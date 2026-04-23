a = 0


n = int(input("Введите число n: "))


while a <= n:
   if 5 <= a <= 9 or 17 <= a <= 37 or 78 <= a <= 87:
       a += 1
       continue
   else:
       print(a)
       a += 1
