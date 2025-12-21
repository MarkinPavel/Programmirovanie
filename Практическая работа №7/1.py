rating = int(input("Введите рейтинг продукта от 1 до 10: "))

match rating:
    case 9 | 10:
        description = "Отличный продукт"
        emoji = "👍"
        recommendation = "Настоятельно рекомендую!"
    case 7 | 8:
        description = "Хороший продукт"
        emoji = "👌"
        recommendation = "Рекомендую"
    case 5 | 6:
        description = "Средний продукт"
        emoji = "🤔"
        recommendation = "Можно попробовать"
    case 3 | 4:
        description = "Ниже среднего"
        emoji = "🙄"
        recommendation = "Подумайте дважды"
    case 1 | 2:
        description = "Плохой продукт"
        emoji = "❌"
        recommendation = "Не рекомендую"
    case _:
        description = "Некорректный рейтинг"
        emoji = "❓"
        recommendation = "Введите число от 1 до 10"

print(f"{description}! {emoji} {recommendation}")