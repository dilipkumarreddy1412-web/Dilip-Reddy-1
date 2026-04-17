from datetime import datetime
now=datetime.now()
print(now)


from datetime import datetime
now=datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))


from datetime import date
today=date.today()
print(today)


from datetime import datetime
current_time=datetime.now().strftime("%H:%M:%S")
print(current_time)
