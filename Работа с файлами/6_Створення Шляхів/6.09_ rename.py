from pathlib import Path

original_path = Path("/Users/alx_it/Documents/Git/First_repo/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)
