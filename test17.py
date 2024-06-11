# Пустой словарь data
data = {}

# Словарь с информацией info
info = {"status": "student", "school": "GoIT"}

# Добавление ключа "name" с вашим именем
data['name'] = "Alex"

# Добавление ключа "age" с вашим возрастом
data['age'] = 32

# Добавление ключа "hobbies" со списком ваших хобби
data['hobbies'] = ["Учиться кодить"]

# Получение возраста из словаря data
age = data.get('age')

# Расширение словаря data значениями из словаря info
data.update(info)

# Печать итогового словаря data
print(data)
