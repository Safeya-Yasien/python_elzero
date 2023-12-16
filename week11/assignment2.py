# https://elzero.org/python-assignments-lesson-from-79-to-80/
# Date & Time

# task 1

import datetime

previous_date = datetime.date(2021, 6, 25)
today = datetime.date(2021, 8, 10)

print((today - previous_date).days)



print("*" * 50)
# task 2

import datetime

# 2023-12-14 13:05:49.685816
print(datetime.datetime.now())
print(datetime.date.today())
current_date = datetime.date.today()
print(current_date.strftime("%b %d, %y"))
print(current_date.strftime("%d - %b - %Y"))
print(current_date.strftime("%d / %b / %y"))
print(current_date.strftime("%d / %B / %Y"))
print(current_date.strftime("%a, %d %B %Y"))
print("*" * 50)












