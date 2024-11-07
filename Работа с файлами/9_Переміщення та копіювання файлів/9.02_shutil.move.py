import shutil
from pathlib import Path

# Вихідний і цільовий шляхи
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Переміщення файла
shutil.move(source, destination)
