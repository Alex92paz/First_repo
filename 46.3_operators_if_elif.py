print("№ 3 -----------------------------")
work_experience = int(input("Enter your full work experience in years: "))

if work_experience <= 1:
    developer_type = "Junior"
    print(f" developer_type - Junior")

elif work_experience <= 5:
    developer_type = "Middle"
    print(f" developer_type - Middle")

else:
    developer_type = "Senior"
    print(f" developer_type - Senior")