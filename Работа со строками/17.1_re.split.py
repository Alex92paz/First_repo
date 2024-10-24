'''
Функция re.split() в модуле re Python используется для разбивания строки по заданному
регулярному выражению. Это позволяет разделять текст на части по более сложным критериям,
чем простой строчный метод split().

Синтаксис:
import re 
list_of_elements = re.split(pattern, string )

pattern - регулярное выражение, используемое в качестве разделителя.
string - строка, которую нужно разделить.

Метод возвращает список строк, разделенных по заданному регулярному выражению.
'''

import re 

text = "Python - это простой, но мощный язык программирования." 
pattern = r"\s+" 
words = re.split(pattern, text)
print(words)   # Выведет список слов в строке


'''
В этом примере \s+ соответствует одному или более пробельным символам (пробел, табуляция и т.п.)
'''