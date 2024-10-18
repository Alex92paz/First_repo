from datetime import datetime

month_day = "02/29"
converted_date = datetime.strptime(f"{month_day};1984", "%m/%d;%Y")
print (converted_date)

dt_now = datetime.now()
print(dt_now)
