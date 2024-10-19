from datetime import datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def prepare_user_list(user_data):
    new_list_users = []  # Створюємо список для зберігання користувачів
    for person in user_data:
        # Додаємо ім'я та дату народження до списку
        new_user = {
            'name': person.get('name'),
            'birthday': string_to_date(person.get('birthday'))
        }
        new_list_users.append(new_user)  # Додаємо нового користувача до списку
    return new_list_users  # Повертаємо список

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# Викликаємо функцію та друкуємо результат
result = prepare_user_list(users)
print(result)