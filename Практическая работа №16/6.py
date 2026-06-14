dept1 = set(map(int, input("Ввод 1: ").split()))
dept2 = set(map(int, input("Ввод 2: ").split()))
dept3 = set(map(int, input("Ввод 3: ").split()))

all_ids = set(range(0, 11))  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

present = dept1 | dept2 | dept3

ghosts = all_ids - present

print(" ".join(map(str, sorted(ghosts))))