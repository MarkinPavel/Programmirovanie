marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

five_count = 0
two_count = 0

for i in marks:
   if i == 5:
       five_count += 1
   if i == 2:
       two_count += 1

print(f"Количество пятерок: {five_count}")
print(f"Количество двоек: {two_count}")
