

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
