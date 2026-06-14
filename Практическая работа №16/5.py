log1 = set(input("Ввод 1: ").split())
log2 = set(input("Ввод 2: ").split())
log3 = set(input("Ввод 3: ").split())

in_all_three = log1 & log2 & log3

all_ips = log1 | log2 | log3

result = all_ips - in_all_three

result_sorted = sorted(result)

print(" ".join(sorted(result)))