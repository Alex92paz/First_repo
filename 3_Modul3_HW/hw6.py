from datetime import datetime, date, timedelta

users = [
    {"name": "Bill Gates", "birthday": "1955.10.25"},
    {"name": "Steve Jobs", "birthday": "1955.10.26"},
    {"name": "Jinny Lee", "birthday": "1956.01.02"},
    {"name": "Sarah Lee", "birthday": "1957.09.08"},
    {"name": "Jonny Lee", "birthday": "1958.11.22"},
    {"name": "John Doe", "birthday": "1985.10.30"},
    {"name": "Jane Smith", "birthday": "1990.11.19"}
]

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:  # Если это суббота или воскресенье
        return find_next_weekday(birthday, 0)  # Переносим на ближайший понедельник
    return birthday

def get_upcoming_birthdays(users, days=90):
    upcoming_birthdays = []
    today = date.today()
    future_date = today + timedelta(days=days)
    
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Если день рождения уже прошел в этом году, переносим его на следующий
        if birthday_this_year < today:
            birthday_next_year = user["birthday"].replace(year=today.year + 1)
            if today <= birthday_next_year <= future_date:
                adjusted_birthday = adjust_for_weekend(birthday_next_year)
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": date_to_string(adjusted_birthday)
                })
        elif today <= birthday_this_year <= future_date:  # Проверяем, попадает ли день рождения в ближайшие дни
            adjusted_birthday = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(adjusted_birthday)
            })
    return upcoming_birthdays

prepared_users = prepare_user_list(users)
upcoming_birthdays = get_upcoming_birthdays(prepared_users, 90)
print(upcoming_birthdays)