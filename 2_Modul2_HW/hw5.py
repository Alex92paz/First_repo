message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0

for char in message:  # Используем другую переменную для цикла
    if char == search:
        result += 1

print(result)