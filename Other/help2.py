# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
#     print("The Student did well")
# else:
#     is_next = False
#     print("The Student did not well")

# num = int(input("Enter a number: "))
'-----------------------------------'

# if num > 0:
#     if num %2 :
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"      
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(f"{result}")  

'-----------------------------------'
# password = 600

# def security(passwd):
#     def divide():
#         nonlocal passwd
#         print(password)
#         return passwd /2
#     return divide()

# print(security(password))
        
'-----------------------------------'
def format_string(string, length):
    if len(string) > length:
        return string
    else:
        total_spaces = length - len(string)
        space_left = total_spaces // 2
        space_right = total_spaces - space_left
        return " " * space_left + string + " " * space_right

result = format_string("cat", 30)  # вызов функции
print(result)  # вывод результата
