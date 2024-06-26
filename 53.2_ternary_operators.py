'''
У прикладі нижче, вираз state = "nice" if is_nice else
"not nice" використовує тернарний оператор для присвоєння
рядка "nice" змінній state, якщо is_nice є істинним True,
і рядка "not nice", якщо is_nice є неправдивим False:
'''
is_nice = False
state = "nice" if is_nice else "not nice"
print(state)

'''
У цьому прикладі значенням змінної state буде рядок 'nice'.
Такий підхід дозволяє швидко перевірити умову, а не писати
декілька рядків оператора if ... else .... Для порівняння,
ось як виглядав би той самий вираз без використання тернарного
оператора, а з використанням стандартного блоку if-else:
'''

is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"
print(state)