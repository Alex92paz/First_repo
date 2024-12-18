import re

text = "Мой адрес электронной почты: example@example.com" 
pattern = r"\w+@\w+\.\w+" 
match = re.search(pattern, text)

if  match :
    print ( "Электронный адрес:" , match .group())


'''
В этом примере регулярное выражение \w+@\w+\.\w+ищет электронный адрес:

\w+  сначала должны идти одна или более букв или цифр.
@    далее обязательно должен быть символ @.
\w+  после символа @должна идти еще одна серия букв.
\.   серия букв должна закончиться символом точки. Мы экранируем его, потому что в регулярном выражении точка является модификатором и имеет специальное значение.
\w+  далее следует серия букв после точки.


'''