while True:
    number = input("Введите число: ")  # Запрашиваем у пользователя число
    number = int(number)  # Преобразуем введённое значение в целое число
    while True:
        print(number)  # Выводим текущее число
        number = number - 1  # Уменьшаем число на 1
        if number < 0:  # Если число стало меньше 0
            break  # Выходим из внутреннего цикла
