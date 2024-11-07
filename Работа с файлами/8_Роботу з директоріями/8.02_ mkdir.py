from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)


'''
Для створення нової директорії використовується метод mkdir().

Path.mkdir(mode=0o777, parents=False, exist_ok=False)

mode - права доступу до директорії, використовуються для Linux і не актуальні для Windows.
parents - якщо має значення True, створить всі батьківські директорії, які відсутні.
exist_ok - якщо має значення True, помилка не буде викинута, якщо директорія вже існує.
'''