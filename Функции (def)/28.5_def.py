def first(size, *args):
    return size + len(args)

def second(size, **kwargs):
    return size + len(kwargs)

# Використання функції first з різними кількостями позиційних аргументів
print(first(5, "first", "second", "third"))  # Результат: 8, оскільки 5 + 3 (три додаткові аргументи)
print(first(1, "Alex", "Boris"))             # Результат: 3, оскільки 1 + 2 (два додаткові аргументи)

# Використання функції second з різними кількостями ключових аргументів
print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6, оскільки 3 + 3 (три ключових аргументи)
print(second(10, comment_one="Alex", comment_two="Boris")) # Результат: 12, оскільки 10 + 2 (два ключових аргументи)
