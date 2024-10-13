age = input("Сколько вам лет? ")
try:
    age = int(age)
    if age >= 18:
        print("Вы взрослый.")
    else:
        print("Вы несовершеннолетний.")
except ValueError:
    print(f"{age} не является числом.")