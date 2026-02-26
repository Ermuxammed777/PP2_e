#Ex Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x)

#Ex Get the year, month, day, hour, minute, second and microsecond:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)

#Ex Return the name of the weekday:
import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))

import datetime
n = datetime.date.today()
print(n.today)