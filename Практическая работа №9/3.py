price = int(input("Цена за услугу: "))


coins = [25, 10, 5, 1]
count = 0
i = 0


while price > 0:
   if price >= coins[i]:
       price -= coins[i]
       count += 1
   else:
       i += 1


print(count)