from pathlib import Path

# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Зміна імені файлу
new_path = original_path.with_suffix(".md")
print(new_path)
