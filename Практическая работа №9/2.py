found_alexandra = False
between_count = 0

while True:
    name = input()

    if name == "Александра":
        found_alexandra = True
        continue

    if name == "Левон":
        break

    if found_alexandra:
        between_count += 1

print(between_count)