print("Калькулятор налогов\n")

TAX_RATE = 0.13

income = float(input("Введите годовой доход: "))

tax_amount = income * TAX_RATE
salary = income - tax_amount

formatted_net_income = f"{income:.2f}".replace(",", " ")
formatted_tax_amount = f"{tax_amount:.2f}".replace(",", " ")
formatted_salary = f"{salary:.2f}".replace(",", " ")

print(f"Общая сумма дохода: {formatted_net_income} руб.")
print(f"Сумма расчитанного налога {formatted_tax} руб.")
print(f"Сумма 'на руки' после вычета налога: {formatted_salary} руб.")