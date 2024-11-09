from pathlib import Path

file_path = Path("/Users/alx_it/Documents/Git/First_repo/example.bin")

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")
