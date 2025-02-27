#Write a Python program to print yesterday, today, tomorrow.

import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(yesterday.strftime('%Y-%m-%d'))
print(today.strftime('%Y-%m-%d'))
print(tomorrow.strftime('%Y-%m-%d'))
