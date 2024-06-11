# Исходные списки
data = [1, 3.11]
some_data = ['python']

# Шаг 1: Добавление списка some_data к списку data
data.extend(some_data)

# Шаг 2: Добавление строки 'python' в позицию с индексом 1
data.insert(1, 'python')

# Шаг 3: Разворот списка data
data.reverse()

# Вывод итогового списка
print(data)
