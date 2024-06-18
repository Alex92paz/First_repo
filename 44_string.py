'''
Впорядкована послідовність означає, що до
елементів рядка можна звертатися за індексом:
'''
s = "Hello world!"
print("№1")
print(s[0])# H
print(s[-1])# !
#--------------------------------------------
'''
Незмінна послідовність означає, що якщо рядок
уже створений, то змінити його не можна, можна
тільки створити новий.
'''
#s = "Hello world!"
#s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError
#--------------------------------------------
'''
Для того, щоб усі літери рядка перевести у верхній
регістр, використовується метод upper
'''
print("№2")
s = "Hello" 
print(s.upper()) # Виведе 'HELLO'
#--------------------------------------------
'''
Для переведення в нижній регістр використовується
метод lower():
'''
print("№3")
s = "Some Text"
print(s.lower())  # Виведе 'some text'
#--------------------------------------------
'''
Щоб перевірити, що рядок починається з підрядка, є
метод startswith:
'''
print("№4")
s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True
#--------------------------------------------
'''
Чтобы проверить, что строка заканчивается подстрокой,
используется метод  endswith:
Этот способ удобно использовать для проверки расширения
файлов.
'''
print("№5")
s = "hello.jpg" 
print (s.endswith( "jpg" )) # Выведет True
#--------------------------------------------
'''
Метод capitalize делает первый символ строки заглавной
буквой, а другие — строчными.
'''
print("№6")
s = "hello world" .capitalize()   # Результат: "Hello world"
print(s)
#--------------------------------------------
'''
Метод title превращает первые буквы каждого слова в строке в прописные:
'''
print("№7")
s = "hello world" .title()   # Результат: "Hello World"
print(s)
#--------------------------------------------
'''
Еще могут пригодиться методы isdigit, isalpha, isspace, которые проверяют,
состоит ли строка только из цифр, букв, пробелов и т.д.
'''
print("№8")
"123" .isdigit() # проверяет, являются ли все символы в строке "123" цифрами. Это возвращает True, потому что все символы являются цифрами. 
"hello" .isalpha() # проверяет, являются ли все символы в строке "hello" буквами. Это возвращает True, потому что все символы являются буквами. 
" " .isspace() # проверяет, являются ли все символы в строке " " (пробел) пробельными символами. Это возвращает True, потому что строка состоит только из пробела.

print("123".isdigit())  # True
print("hello".isalpha())  # True
print(" ".isspace())  # True

#--------------------------------------------
'''
До появления  f строк в Python активно использовали метод  format.
Метод  format в Python используется для форматирования строк. Он заменяет
{} в строке на аргументы, передаваемые методу  format. Это очень полезно
для создания динамических строк.
'''
print("№8")
# Простое форматирование строки 
name = 'John' 
print ('Hello, {}!' .format(name))

# Форматирование с несколькими аргументами
age = 25
print ('Hello, {}. Вы {} years old.' .format(name, age))

# Использование именуемых аргументов 
print ('Hello, {name}. You are {age} years old.' .format( name = 'Jane' , age =30))

# Использование индексов для указания порядка аргументов 
print ('Hello, {1}. You are {0} years old.' .format(age, name))
#--------------------------------------------
'''
Срезы в Python — это мощный механизм для доступа к частям
последовательностей, таких как строки, списки и кортежи!
Срезы определяются с помощью квадратных скобок [] с указанием
индексов начала, конца и (необязательно) шага. Вот основной синтаксис:
последовательность [начало:конец:шаг]
'''
print("№9")
s = "Hello, World!"
first_five = s[:5]
print(first_five)   # Выведет 'Hello'
#--------------------------------------------
print("№10")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
odd_numbers_1 = numbers[ 0 : 10 : 2 ]
odd_numbers_2 = numbers[:: 2 ]   # Выведет [1, 3, 5, 7, 9]
print(odd_numbers_1)
print(odd_numbers_2)

'''
В  even_numbers мы берем числа, начиная с индекса 1до 10с шагом 2и получим
список [2, 4, 6, 8, 10]. Здесь тоже можно сократить запись среза и записать.
'''
even_numbers = numbers[ 1 :: 2 ] # Выведет [2, 4, 6, 8, 10]
print(even_numbers)

'''
И, наконец, получим числа списка, кратные трем.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
three_numbers = numbers[ 2 : 10 : 3 ]
print(three_numbers)