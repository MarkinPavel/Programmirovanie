nominals = [5000, 2000, 1000, 500, 200, 100]

print("Банкомат с номиналами: 5000, 2000, 1000, 500, 200, 100")
print("Сумма должна быть кратной 100")

try:
   amount = int(input("Введите сумму для снятия (кратную 100): "))
   if amount <= 0 or amount % 100 != 0:
       print("Сумма введена некорректно")
   else:
       print(f"\nВы запросили: {amount} руб.")
       print("=" * 30)

       count_5000 = amount // 5000
       remaining = amount - count_5000 * 5000

       count_2000 = remaining // 2000
       remaining = remaining - count_2000 * 2000

       count_1000 = remaining // 1000
       remaining = remaining - count_1000 * 1000

       count_500 = remaining // 500
       remaining = remaining - count_500 * 500

       count_200 = remaining // 200
       remaining = remaining - count_200 * 200

       count_100 = remaining // 100

       total_issued = 0
       issued = False

       if count_5000 > 0:
           print(f"Купюр номиналом 5000 руб.: {count_5000} шт.")
           total_issued += count_5000 * 5000
           issued = True

       if count_2000 > 0:
           print(f"Купюр номиналом 2000 руб.: {count_2000} шт.")
           total_issued += count_2000 * 2000
           issued = True

       if count_1000 > 0:
           print(f"Купюр номиналом 1000 руб.: {count_1000} шт.")
           total_issued += count_1000 * 1000
           issued = True

       if count_500 > 0:
           print(f"Купюр номиналом 500 руб.: {count_500} шт.")
           total_issued += count_500 * 500
           issued = True

       if count_200 > 0:
           print(f"Купюр номиналом 200 руб.: {count_200} шт.")
           total_issued += count_200 * 200
           issued = True

       if count_100 > 0:
           print(f"Купюр номиналом 100 руб.: {count_100} шт.")
           total_issued += count_100 * 100
           issued = True

       if not issued:
           print("Не удалось выдать запрошенную сумму доступными номиналами")
       elif total_issued == amount:
           print(f"Сумма {total_issued} руб. выдана полностью!")
       else:
           print(f"Ошибка в расчетах! Выдано {total_issued} из {amount} руб.")

except ValueError:
   print("Ошибка, введите целое число.")
