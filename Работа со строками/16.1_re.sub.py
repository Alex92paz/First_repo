'''
Метод sub
Метод re.sub() в модуле re Python используется для замены вхождений регулярного
выражения pattern в строке string на строку repl. Это очень полезно для изменения текста.

import re 
modified_string = re.sub(pattern, repl, string)

pattern - регулярное выражение, указывающее часть строки, которую нужно заменить.
repl - строка, на которую будут заменены совпадения.
string - строка, в которой происходит замена.
'''
import re 

file_name = "Мой документ Python.txt" 
pattern = r"\s" 
replacement = "_" 
formatted_name = re.sub(pattern, replacement, file_name) 
print(formatted_name)  

'''
В этом примере блок \s соответствует любому пробельному символу, и он заменяется на _.
'''