from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday=0):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7

    return start_date + timedelta(days=days_ahead)
      

def adjust_for_weekend(birthday):

    if birthday.weekday() >= 5:
        return find_next_weekday(birthday)
    else:
        return birthday

    


start_date = string_to_date("2024.01.06")  # Перетворення рядка на дату
resolt = adjust_for_weekend(start_date)
print(resolt)
print(resolt.weekday())

