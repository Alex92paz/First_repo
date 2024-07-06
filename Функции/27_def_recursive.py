
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)
    
num = 3
print(f"Факториал {num} это {factorial_recursive(num)}")

'''
3 * (3-1) * ((3-1)-1)  # так как 3-1-1 равно 1, рекурсия остановилась
'''