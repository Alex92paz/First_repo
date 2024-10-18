def format_string(string, length):
    if len(string) > length:
        return string
    else:
        total_spaces = length - len(string)
        space_left = total_spaces // 2
        space_right = total_spaces - space_left
        return " " * space_left + string + " " * space_right

result = format_string("cat", 30)  # вызов функции
print(result)  # вывод результата