# f"{value: < ширина > . < точность > %}"
'''
где:
value – значение, которое нужно превратить в проценты.
< ширина > - общая ширина поля; необязательно.
< точність > - количество знаков после десятичной точки; необязательно.
'''

completion = 0.756 
formatted = f"{completion:.1%}" 
print (formatted) # Выведет: ' 75.6%'


progress = 0.5
formatted = f"{progress:.0%}"
print(formatted)
