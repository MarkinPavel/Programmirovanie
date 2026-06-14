input_string = input("Введите целые числа : ")

numbers_str = input_string.split()

numbers = []
for num_str in numbers_str:
   numbers.append(int(num_str))

pairs_count = 0
i = 0

while i < len(numbers) - 1:
   if numbers[i] == numbers[i + 1]:
       pairs_count += 1
       i += 2
   else:
       i += 1

print(f"Количество пар: {pairs_count}")
