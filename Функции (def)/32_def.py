def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        total_space = length - len(string)
        left_space = total_space // 2
        right_space = total_space - left_space 
        return f"{' ' * left_space}{string}{' ' * right_space}"


string = input("Введите слово: ")
length = int(input("Введите число: "))


resolt = format_string(string, length)
print(f"'{resolt}'")
print(len(resolt))