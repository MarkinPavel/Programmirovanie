word = str(input("Введите слово: "))

word = list(word)

word2 = word[::-1]

if word == word2:
   print("Это палиндром")
else:
   print("Не палиндром")
