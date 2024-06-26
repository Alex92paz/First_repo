print("№ 1 -----------------------------")
num = 15  # приклад значення для num

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")

print("№ 2 -----------------------------")
x = int(input('Введіть число: '))

if x % 2 == 0:
    print("Число x є парним.")
else:
    print("Число x є непарним.")

print("№ 3 -----------------------------")
is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
    print("Кандидат проходить до наступного туру")
else:
    is_next = False
    print("Кандидат не проходить до наступного туру")
