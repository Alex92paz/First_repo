pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = round(pool/quantity)
except ZeroDivisionError:
    print('Сannot be divided by zero!')
else:
    print(chunk)