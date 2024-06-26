def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    if k > n:
        return 0
    
    n_factorial = factorial(n)
    k_factorial = factorial(k)
    n_minus_k_factorial = factorial(n - k)
    
    return n_factorial // (n_minus_k_factorial * k_factorial)

# Пример использования:
n = 50  # общее количество подписчиков
k = 7   # количество призов
result = number_of_groups(n, k)
print(f"Количество различных списков победителей: {result}")
