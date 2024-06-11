first_name = "John"
last_name = "Doe"

def get_fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

# Вызов функции и вывод результата
full_name = get_fullname(first_name, last_name)
print(full_name)
print(len(full_name))

length = len(full_name)
print(full_name[0])
print(full_name[length - 1])