from datetime import datetime, timedelta

def string_to_date(date_string):
    # Використовуємо метод strptime для перетворення рядка на об'єкт datetime
    date_object = datetime.strptime(date_string, "%Y.%m.%d").date()
    return date_object

def find_next_weekday(start_date, weekday=0):
    # Визначення дня тижня start_date (понеділок = 0, вівторок = 1, ..., неділя = 6)
    current_weekday = start_date.weekday()
    # Обчислення різниці між поточним днем тижня та бажаним днем тижня
    days_ahead = weekday - current_weekday
    
    # Якщо результат менше або дорівнює 0, це означає, що бажаний день тижня уже минув у цьому тижні,
    # тому додаємо 7 днів для переходу до наступного тижня
    if days_ahead <= 0:
        days_ahead += 7
    
    # Додаємо обчислену кількість днів до початкової дати
    next_weekday = start_date + timedelta(days=days_ahead)
    
    return next_weekday

start_date = string_to_date("2022.01.01")  # Перетворення рядка на дату
print(start_date, start_date.weekday())

next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
print(next_monday, next_monday.weekday())

next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
print(next_friday, next_friday.weekday())