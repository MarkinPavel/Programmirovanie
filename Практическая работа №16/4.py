cia = input("Ввод (ЦРУ): ").split()
mi6 = input("Ввод (МИ-6): ").split()
kgb = input("Ввод (КГБ): ").split()

set_cia = set(cia)
set_mi6 = set(mi6)
set_kgb = set(kgb)

double_agents = (set_cia & set_mi6) - set_kgb

result = sorted(double_agents, reverse=True)

print(" ".join(sorted(result)))