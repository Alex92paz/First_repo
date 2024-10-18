import math

# Исходное число 
x = 3.71

# Использование различных методов округления 
ceil_result = math .ceil(x)   # Округление вверх 
floor_result = math .floor(x)   # Округление вниз 
trunc_result = math .trunc(x)   # Отсечение дробной части

print(ceil_result, floor_result, trunc_result, sep="\n")