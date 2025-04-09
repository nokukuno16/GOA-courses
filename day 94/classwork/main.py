numbers = [24, 36, 5, 18, 55, 48, 100, 12]
filtered_numbers = list(filter(lambda x: x % 12 == 0, numbers))
print(filtered_numbers)