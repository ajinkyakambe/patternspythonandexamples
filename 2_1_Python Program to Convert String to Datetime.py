# 1. Python Program to Convert String to Datetime

from datetime import datetime

my_date_string = "Aug 17 2022 11:31AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)