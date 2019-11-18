from datetime import datetime

from dummydate import date_to_check

year_to_check = date_to_check.get('year')
month_to_check = date_to_check.get('month')
day_to_check = date_to_check.get('day')
hour_to_check = date_to_check.get('hour')
minute_to_check = date_to_check.get('minute')

now = datetime.now()
input_date = datetime(year_to_check, month_to_check, day_to_check, hour_to_check, minute_to_check)

def compare_dates(now, input_date):
    if now >= input_date:
        return 'Ese momento ya ha pasado'
    else:
        return 'Todavía no hemos llegado'
    
result = compare_dates(now, input_date)
print(result)