# в залежності від оцінки визначити коментар викладача до роботи:
# >= 90: Excellent!
# 75-89 Well done!
# 60-74: You can do better.
# Інша: You don't pass the exam.

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Excellent!")
elif grade >= 75:
    print("Well done!")
elif grade >= 60:
    print("You can do it better.")
else:
    print("You don't pass the exam.")