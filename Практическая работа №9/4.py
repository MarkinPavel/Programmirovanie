number = int(input("Введите натуральное число: "))

count_digit_3 = 0
count_last_digit = 0
count_even_digits = 0
sum_greater_5 = 0
product_greater_7 = 1
count_0_and_5 = 0

last_digit = number % 10
temp_number = number
found_digit_greater_7 = False

while temp_number > 0:
    digit = temp_number % 10

    if digit == 3:
        count_digit_3 += 1

    if digit == last_digit:
        count_last_digit += 1

    if digit % 2 == 0:
        count_even_digits += 1

    if digit > 5:
        sum_greater_5 += digit

    if digit > 7:
        product_greater_7 *= digit
        found_digit_greater_7 = True

    if digit == 0 or digit == 5:
        count_0_and_5 += 1

    temp_number //= 10

if not found_digit_greater_7:
    product_greater_7 = 1

print(f"Количество цифр 3: {count_digit_3}")
print(f"Сколько раз встречается последняя цифра {last_digit}: {count_last_digit}")
print(f"Количество чётных цифр: {count_even_digits}")
print(f"Сумма цифр, больших пяти: {sum_greater_5}")
print(f"Произведение цифр, больших семи: {product_greater_7}")
print(f"Сколько раз встречаются цифры 0 и 5 (суммарно): {count_0_and_5}")