from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

# У цьому прикладі, Path("documents/example.txt") створює відносний шлях.
# Метод absolute() перетворює його в абсолютний шлях, виходячи з поточного робочого каталогу.