import re

text = "Изучение Python может быть веселым." 
pattern = "Python" 
match = re.search(pattern, text)

if  match:
    print ("Найдено:" ,match.group())
else:
    print ("Не найдено.")
