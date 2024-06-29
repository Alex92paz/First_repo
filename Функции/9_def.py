def modify_list (lst: list) -> None :
    lst = lst. copy ()    # Создаем копию списка
    lst. append ( 4 )     # Изменяем копию

my_list = [ 1 , 2 , 3 ]
modify_list (my_list)     # вызов функции
print (my_list)           # выведет: [ 1 , 2 , 3 ]

'----------------------------------------'

def modify_list (lst: list) -> None :
    lst = lst. copy ()    # Создаем копию списка
    lst. append ( 4 )     # Изменяем копию
    print(lst)            # Выводим измененную копию

my_list = [ 1 , 2 , 3 ]   
modify_list (my_list)     # вызов функции

