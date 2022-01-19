import datetime

year = int(datetime.date.today().strftime('%Y'))
month = int(datetime.date.today().strftime('%m'))
date = int(datetime.date.today().strftime('%d'))
current_date = datetime.date(year, month, date).strftime("%Y%m%d")
print(year)
print(month)
print(date)
print(current_date)