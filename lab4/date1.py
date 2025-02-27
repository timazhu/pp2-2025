#Write a Python program to subtract five days from current date.

import datetime
dt_now = datetime.datetime.now()
dt_minus_5 = dt_now - datetime.timedelta(days=5)
print(dt_minus_5)

#2025-02-22 23:23:53.073494