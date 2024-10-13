# try:   
#     work_experience = int(input("Enter your full work experience in years: "))
# except ValueError:
#     print("You entered an invalid integer! Let's try with a float value.")
#     try:
#         work_experience = float(input("Enter your full work experience in years: "))
#     except ValueError:
#         print("Invalid input! You didn't enter a valid number.")
#         work_experience = None  # If the second input is also invalid, set work_experience to None

# if work_experience is not None:
#     if 1 < work_experience <= 5:
#         developer_type = "Middle"
#         print(f'You are {developer_type}! **')
#     elif work_experience <= 1:
#         developer_type = "Junior"
#         print(f'You are {developer_type}! *')
#     else:
#         developer_type = "Senior"
#         print(f'You are {developer_type}! ***')

try:   
    work_experience = int(input("Enter your full work experience in years: "))
except ValueError:
    print("You entered an invalid integer! Let's try with a float value.")
    try:
        work_experience = float(input("Enter your full work experience in years: "))
    except ValueError:
        print("Invalid input! You didn't enter a valid number.")
        work_experience = None  # If the second input is also invalid, set work_experience to None

if work_experience is not None:
    if 1 < work_experience <= 5:
        developer_type = "Middle"
        print(f'You are {developer_type}! **')
    elif work_experience <= 1:
        developer_type = "Junior"
        print(f'You are {developer_type}! *')
    else:
        developer_type = "Senior"
        print(f'You are {developer_type}! ***')