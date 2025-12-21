SEATS_PER_COMPARTMENT = 4

seat_number = int(input("Введите номер места "))

if seat_number > 36:
    print("Ошибка, в вагоне всего 36 мест")

else:
    seat_compartment = (seat_number - 1) // SEATS_PER_COMPARTMENT + 1

    print(f"Номер места {seat_number} находится в купе {seat_compartment}")
