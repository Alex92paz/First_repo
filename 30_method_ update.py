my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@example.com", "age": 26})

print(my_dict)

'''
Метод update() використовується для оновлення словника іншим
словником або парами ключ-значення. Якщо в вас є словник 
my_dict = {"name": "Alice", "age": 25} і ви виконаєте 
my_dict.update({"email": "alice@example.com", "age": 26}),
то словник my_dict буде оновлено новими парами ключ-значення,
де ключ "email" буде додано в словник, а значення ключа "age" буде оновлено.
'''