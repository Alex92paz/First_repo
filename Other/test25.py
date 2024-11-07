# Создание пустого словаря
cat = {}

# Добавление ключа "nick"
cat['nick'] = 'Simon'

# Добавление ключа "age"
cat['age'] = 7

# Добавление ключа "characteristics"
cat['characteristics'] = ["лагідний", "кусається"]

# Объявление словаря с дополнительной информацией
info = {"status": "vaccinated", "breed": True}

# Использование метода get для получения возраста кота
age = cat.get('age')

# Использование метода update для добавления всех пар ключ-значение из словаря info
cat.update(info)

# Вывод словаря cat
print(cat)
