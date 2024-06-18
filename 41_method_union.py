'''
Об'єднання двох множин включає всі елементи з обох множин,
але без дублікатів. Це знаходиться за допомогою оператора
| або методу union:
'''

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
