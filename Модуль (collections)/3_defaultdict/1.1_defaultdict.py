from collections import defaultdict

# Создание defaultdict из list как фабрикой по умолчанию 
d = defaultdict(list)

# Добавление элементов в список для каждого ключа 
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
