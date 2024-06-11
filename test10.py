text = "Hello, world! Welcome to the world of Python."

# Найти позицию первого вхождения подстроки "world"
position = text.find("world")
print(position)  # Выводим позицию

# Заменить все вхождения "world" на "planet"
updated_text = text.replace("world", "planet")

# Выводим обновленный текст
print(updated_text)
