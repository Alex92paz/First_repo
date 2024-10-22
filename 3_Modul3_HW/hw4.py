from datetime import datetime, timedelta, date

# Список пользователей с датой рождения
users = [
    {"name": "Bill Gates", "birthday": "1955.10.25"},
    {"name": "Steve Jobs", "birthday": "1955.11.21"},
    {"name": "Jinny Lee", "birthday": "1956.10.22"},
    {"name": "John Doe", "birthday": "1985.09.23"},
    {"name": "Jane Smith", "birthday": "1990.11.27"}
]

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date_obj):
    return date_obj.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    new_list_users = []
    
    for user in user_data:
        birthday = string_to_date(user.get('birthday'))
        new_user = {
            'name': user.get('name'),
            'birthday': birthday  # Оставляем только оригинальную дату
        }
        new_list_users.append(new_user)
    
    return new_list_users

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    future_date = today + timedelta(days=days)

    for user in users:
        # Вычисляем день рождения в текущем году
        birthday_this_year = user["birthday"].replace(year=today.year)
        
        if today <= birthday_this_year <= future_date:
            upcoming_birthdays.append({
                "name": user.get("name"),
                "congratulation_date": date_to_string(birthday_this_year)  # Оригинальная дата рождения для вывода
            })
    return upcoming_birthdays

# Вызов функций
prepared_users = prepare_user_list(users)
upcoming_birthdays = get_upcoming_birthdays(prepared_users, 7)

print(upcoming_birthdays)