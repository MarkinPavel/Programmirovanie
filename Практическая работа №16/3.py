server_a = "data.db image.png log.txt"
server_b = "image.png script.py data.db"

set_a = set(server_a.split())
set_b = set(server_b.split())

common = set_a & set_b
lost = set_a - set_b

print("Общие:", " ".join(sorted(common)))
print("Потерянные:", " ".join(sorted(lost)))