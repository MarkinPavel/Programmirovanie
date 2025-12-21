USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Конвертирует сумму из долларов США в российские рубли.

    Параметры:
    amount_usd (float): сумма в долларах США для конвертации.

    Возвращает:
    float: Сумма в российский рублях после конвертации
    """
    return amount_usd * USD_TO_RUB

print("Конвертер долларов в рубли\n")

amount_str =  input("Введите сумму в долларах: ")
amount_usd = float(amount_str)

amount_rub = convert_usd_to_rub(amount_usd)

print("\nРезультат конвертации")
print(f"{amount_usd:.2f} USD = {amount_rub:.2f} RUB")
print(f"По курсу: 1 usd = {USD_TO_RUB} RUB")