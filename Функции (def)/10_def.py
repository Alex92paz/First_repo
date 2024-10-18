def string_to_codes(string: str) -> dict: 
    # функция string_to_codes принимает аргумент string типа str и возвращает значение типа dict
    # string: str: Это аннотация для аргумента string, которая говорит, что ожидается строка (str).
    #-> dict:: Это аннотация для возвращаемого значения функции, которая указывает, что функция возвращает словарь (dict).
    
    # Инициализация словаря для хранения кодов
    codes = {}
    # Перебор каждого символа в строке
    for ch in string:
        # Проверка, есть ли символ в словаре
        if ch not in codes:
            # Добавление пары символ-код в словарь
            codes[ch] = ord(ch)
    return codes

my_string = 'Hello World'  # Используйте строку, а не список
result = string_to_codes(my_string)
print(result)  # Выводим результат работы функции