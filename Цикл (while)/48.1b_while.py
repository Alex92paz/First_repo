num = int(input("Enter the integer (0 to 100): "))
sum = 0

while True:
    if num >= 0:
        sum += num
        num =(num - 1)
    else:
        break

print(sum)
    
    
