month = int(input())
date = int(input())

def check(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        return 28
    else:
        return 30


maxdate = check(month)
tmp = date+1
if tmp > maxdate:
    date = 1
    month += 1
else:
    date += 1

if month == 13 and date == 1:
    print(1)
    print(1)
else:
    print(month)
    print(date)