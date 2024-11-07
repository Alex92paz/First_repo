from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()

current_working_directory = Path("/Users/alx_it/Documents/Git/First_repo/documents/example_for_new_core/l04")
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)

