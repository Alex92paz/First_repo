# Определяем строку, в которой будем искать, и символ, который будем искать
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience"
search = "r"

# Инициализируем переменную для подсчета
result = 0

# Проходим через каждый символ в строке message
for char in message:
    # Если текущий символ совпадает с искомым символом, увеличиваем счетчик
    if char == search:
        result += 1

# Выводим количество вхождений искомого символа
print(f"Символ '{search}' встречается в строке {result} раз(а).")
