# Создание пустого словаря
cat = {}

# Добавление ключа "nick"
cat['nick'] = 'Simon'
print(cat)

# Добавление ключа "age"
cat['age'] = 7
print(cat)

# Добавление ключа "characteristics"
cat['characteristics'] = ["лагідний", "кусається"]
print(cat)

# Объявление словаря с дополнительной информацией
info = {"status": "vaccinated", "breed": True}


# Использование метода get для получения возраста кота
age = cat.get('age')


# Использование метода update для добавления всех пар ключ-значение из словаря info
cat.update(info)
print(cat)

# Вывод словаря cat
print(cat)
