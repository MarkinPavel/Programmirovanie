total_minutes = int(input("Введите кол-во минут: "))

hours = total_minutes // 60

minutes = total_minutes % 60

print(f"{total_minutes} мин - это {hours} час {minutes} минут")