numbers = [43, 4, 358, 7, 93]
print(numbers)

min_number = numbers.index(min(numbers))
numbers[0], numbers[min_number] = numbers[min_number], numbers[0]
print(numbers)
