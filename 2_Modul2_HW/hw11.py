def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        padding = (length - len(string)) // 2
        return " " * padding + string

# Приклади використання функції:
print(format_string("Привіт", 10))  # Очікуваний результат: "  Привіт  "
print(format_string("Центрування", 20))  # Очікуваний результат: "    Центрування    "
print(format_string("Довгий рядок", 5))  # Очікуваний результат: "Довгий рядок" (рядок без змін)
