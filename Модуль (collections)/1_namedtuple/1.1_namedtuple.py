from collections import namedtuple 

# Создание именуемого кортежа 
Point = namedtuple( 'Point' , [ 'x' , 'y' ])


# Создание экземпляра Point
p = Point(11, y =22)
print (p.x) # Доступ к элементам print (px) # 11
print (p.y) # Доступ к элементам print (px) # 22



