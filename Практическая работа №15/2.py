print("ЭТАП 1: База растений")

plants_input = input("Введите данные о растениях (Название цвет размер рост): ")

plants_list = plants_input.split(", ")

print("\nРастения на ферме:")
for plant in plants_list:
    name, color, size, growth = plant.split()
    print(f"{name} {color} {size} {growth}")


print("\nЭТАП 2: Проверка возможности скрещивания")

hybrids_input = input("Введите список гибридов (Название1+Название2=Гибрид): ")

hybrids_dict = {}

if hybrids_input.strip():
    hybrid_pairs = hybrids_input.split(";")
    for pair in hybrid_pairs:
        if "=" in pair:
            parents, child = pair.split("=")
            parent1, parent2 = parents.split("+")

            key = tuple(sorted([parent1.strip(), parent2.strip()]))
            hybrids_dict[key] = child.strip()

plant1 = input("Введите название первого растения: ").strip()
plant2 = input("Введите название второго растения: ").strip()

key = tuple(sorted([plant1, plant2]))

if key in hybrids_dict:
    print(f"Получен гибрид: {hybrids_dict[key]}")
else:
    print("Эти растения нельзя скрестить")

print("\nЭТАП 3.1: Определение цвета гибрида")

print("Введите данные первого родителя: ")
parent1_name = input("Название: ").strip()
parent1_color = input("Цвет: ").strip()
parent1_size = input("Размер (малый/средний/крупный): ").strip()
parent1_growth = input("Скорость роста (быстрый/средний/медленный): ").strip()

print("\nВведите данные второго родителя:")
parent2_name = input("Название: ").strip()
parent2_color = input("Цвет: ").strip()
parent2_size = input("Размер (малый/средний/крупный): ").strip()
parent2_growth = input("Скорость роста (быстрый/средний/медленный): ").strip()

if parent1_name < parent2_name:
    hybrid_color = parent1_color
else:
    hybrid_color = parent2_color

print(f"\nЦвет гибрида: {hybrid_color}")

print("\nЭТАП 3.2: Определение размера гибрида")

size_ranking = {"малый": 1, "средний": 2, "крупный": 3}

if parent1_size == parent2_size:
    hybrid_size = parent1_size
else:
    if size_ranking[parent1_size] < size_ranking[parent2_size]:
        hybrid_size = f"{parent1_size}/{parent2_size}"
    else:
        hybrid_size = f"{parent2_size}/{parent1_size}"

print(f"Размер гибрида: {hybrid_size}")

print("\nЭТАП 3.3: Определение скорости роста гибрида")

growth_ranking = {"быстрый": 3, "средний": 2, "медленный": 1}

if growth_ranking[parent1_growth] < growth_ranking[parent2_growth]:
    hybrid_growth = parent1_growth
else:
    hybrid_growth = parent2_growth

print(f"Скорость роста гибрида: {hybrid_growth}")

print(f"Родитель 1: {parent1_name} ({parent1_color}, {parent1_size}, {parent1_growth})")
print(f"Родитель 2: {parent2_name} ({parent2_color}, {parent2_size}, {parent2_growth})")
print(f"\nХарактеристики гибрида:")
print(f"  Цвет: {hybrid_color}")
print(f"  Размер: {hybrid_size}")
print(f"  Скорость роста: {hybrid_growth}")

key = tuple(sorted([parent1_name, parent2_name]))
if key in hybrids_dict:
    print(f"  Название гибрида: {hybrids_dict[key]}")