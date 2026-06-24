def get_days(month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]

print(get_days(1))
print(get_days(2))
print(get_days(9))