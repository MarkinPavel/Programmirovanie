status = input("Введите статус заказа (pending, processing, shipped, delivered, cancelled): ").strip().lower()

match status:
    case "pending":
        status = "В ожидании"
        emoji = "⏳"
        description = "Ваш заказ ожидает обработки"
        time = "1-2 дня"

    case "processing":
        status = "В обработке"
        emoji = "📦"
        description = "Ваш заказ собирается и упаковывается"
        time = "1-3 дня"

    case "shipped":
        status = "Отправлено"
        emoji = "🚚"
        description = "Ваш заказ находится в пути к вам"
        time = "2-5 дней"

    case "delivered":
        status = "Доставлено"
        emoji = "✅"
        description = "Ваш заказ успешно доставлен"
        time = "0 дней"

    case "cancelled":
        status = "Отменено"
        emoji = "❌"
        description = "Ваш заказ был отменен"
        time = "—"

    case _:
        print(f"❌ Ошибка: Неизвестный статус {status}")
        print("Доступные статусы: pending, processing, shipped, delivered, cancelled")
        exit()

print('#'*39)
print("#      📦 СТАТУС ВАШЕГО ЗАКАЗА 📦    #" )
print('#'*39, '\n')
print(f"Статус: {status} {emoji}")
print(f"Описание: {description}")
print(f"Примерное время: {time}")
print(f"Рекомендация: Следите за уведомлениями о доставке")