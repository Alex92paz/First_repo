def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

# Приклади використання функції:
print(get_fullname("Іван", "Петренко", "Іванович"))  # Очікуваний результат: "Іван Іванович Петренко"
print(get_fullname("Олена", "Коваленко"))           # Очікуваний результат: "Олена Коваленко"
