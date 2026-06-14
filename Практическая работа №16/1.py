words = input("Введите слова через пробел: ").split()

unique_words = set(words)

count = len(unique_words)

sorted_words = sorted(unique_words)

print(f"Количество уникальных слов: {count}")
print(f"Слова: {sorted_words}")
