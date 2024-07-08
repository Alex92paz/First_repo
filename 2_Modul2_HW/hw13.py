import math

def number_of_groups(n, k):
    if k > n:
        return 0
    
    return math.comb(n, k)

# Пример использования:
n = 100  # общее количество подписчиков
k = 99   # количество призов
result = number_of_groups(n, k)
print(f"Количество различных списков победителей: {result}")