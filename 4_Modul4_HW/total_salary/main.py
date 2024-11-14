import random
import pathlib

current_dir = pathlib.Path(__file__).parent

def total_salary(current_dir):
    try:
        with open(current_dir / "info.txt", "r", encoding="utf-8") as file:
            workers = file.readlines()
            resolts = random.choice(workers).strip()  # Убрано "return"
            print(resolts)
    except FileNotFoundError:
        return "Не удалось найти файл."