first_name = "John"
last_name = "Doe"

def get_initials(first_name, last_name):
    formatted_name1 = first_name[0]  # Получаем первую букву имени
    formatted_names2 = f"{last_name} {formatted_name1}."  # Формируем строку с инициалами
    return formatted_names2

# Вызов функции и вывод результата
formatted_names2 = get_initials(first_name, last_name)
print(formatted_names2)
