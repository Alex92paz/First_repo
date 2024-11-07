import shutil
from pathlib import Path

# Вихідний і цільовий файли
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Копіювання файла
shutil.copy(source, destination)


'''
Функція shutil.copy() копіює вміст файлу, але не копіює метадані,
тоді як shutil.copy2() копіює і вміст, і метадані.
'''