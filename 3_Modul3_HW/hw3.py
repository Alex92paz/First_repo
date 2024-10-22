from datetime import datetime, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, weekday):
    if  weekday == 0:
        if start_date.weekday() == 0:
            end_date = start_date + timedelta(weeks=1)
            return end_date
        elif start_date.weekday() == 1:
            end_date = start_date + timedelta(days=6)
            return end_date
        elif start_date.weekday() == 2:
            end_date = start_date + timedelta(days=5)
            return end_date
        elif start_date.weekday() == 3:
            end_date = start_date + timedelta(days=4)
            return end_date
        elif start_date.weekday() == 4:
            end_date = start_date + timedelta(days=3)
            return end_date
        elif start_date.weekday() == 5:
            end_date = start_date + timedelta(days=2)
            return end_date
        elif start_date.weekday() == 6:
            end_date = start_date + timedelta(days=1)
            return end_date

    if  weekday == 4:
        if start_date.weekday() == 0:
            end_date = start_date + timedelta(days=4)
            return end_date
        elif start_date.weekday() == 1:
            end_date = start_date + timedelta(days=3)
            return end_date
        elif start_date.weekday() == 2:
            end_date = start_date + timedelta(days=2)
            return end_date
        elif start_date.weekday() == 3:
            end_date = start_date + timedelta(days=1)
            return end_date
        elif start_date.weekday() == 4:
            return start_date
        elif start_date.weekday() == 5:
            end_date = start_date + timedelta(days=6)
            return end_date
        elif start_date.weekday() == 6:
            end_date = start_date + timedelta(days=5)
            return end_date

start_date = string_to_date("2022.01.03")  # Перетворення рядка на дату
print(start_date, start_date.weekday())

next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
print(next_monday, next_monday.weekday())
next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
print(next_friday, next_friday.weekday())