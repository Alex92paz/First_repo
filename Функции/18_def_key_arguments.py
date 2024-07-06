def real_cost ( base : int , discount: float = 0 ) -> float :
     return  base * ( 1 - discount )

price_bread = 15 
price_butter = 50 
price_sugar = 60 

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05 )
current_price_sugar = real_cost(price_sugar, 0.30)

print (f'Новая стоимость хлеба: {current_price_bread}' ) 
print (f'Новая стоимость масла: {current_price_butter}' ) 
print (f'Новая стоимость сахара: {current_price_sugar}' )
