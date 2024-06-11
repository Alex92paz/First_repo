first = "Python"
second = "python"

def compare(first, second):
    # Приводим обе строки к нижнему регистру и сравниваем их
    return first.lower() == second.lower()

# Вызов функции и сохранение результата
result = compare(first, second)

# Вывод результата
print(result)
