my_dict = {"name": "Alex", "age": 32, "city": "Tel Aviv", "email": "alex1992paz@gmail.com"}

new_dict = my_dict.copy()

print(new_dict)

'''
Метод copy() створює поверхневу копію словника.
Якщо використати new_dict = my_dict.copy(), то new_dict 
буде новим словником з тими самими парами ключ-значення,
що і my_dict, але як окремий об'єкт.
'''