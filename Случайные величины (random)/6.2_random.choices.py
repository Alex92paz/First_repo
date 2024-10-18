import random

colors = [ 'красный' , 'зеленый' , 'синий' ] 
weights = [10, 1, 1] 
chosen_color = random .choices (colors, weights, k= 1)
print (chosen_color)  
