x = 50

def func () :
     global x
     print( 'x равно' , x)   # x равно 50 
     x = 2 
     print( 'Изменяем глобальное значение x на' , x)   # Изменяем глобальное значение x на 2

func () 
print( 'Значение x составляет' , x) # Значение x составляет 2

