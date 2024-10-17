def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# Функция для вычисления комбинаций C(n, k)
def number_of_groups(n, k):
    if k > n:
        return 0 # Если k больше n, комбинации невозможны
    
    n_factorial = factorial(n)  # Вычисляем n!
    k_factorial = factorial(k)  # Вычисляем k!
    n_minus_k_factorial = factorial(n - k)  # Вычисляем (n - k)!
    return n_factorial // ((n_minus_k_factorial)*k_factorial)

# Пример: C(4, 2) - комбинации для выбора 2 объектов из 5
n = 4  # Общее количество людей
k = 2  # Количество выбранных победителей

result = number_of_groups(n, k)  # Вычисляем количество комбинаций
print(f"C(4, 2) = {result}")  # Вывод результата

# "Ax1" "Ax2" "Ax3" "Ax4"

# 1   2
# 3   4  

# 1   3  
# 2   4

# 1   4
# 2   3   
