def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Alice", "age": 25}
greet(**person_info)

'''
У цьому прикладі **person_info розпаковує словник person_info,
і його ключі та значення передаються як ключові аргументи в функцію greet.
'''