from datetime import datetime


# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
number_day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {number_day_of_week}")
