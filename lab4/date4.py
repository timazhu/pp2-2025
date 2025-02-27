#Write a Python program to calculate two date difference in seconds.

from datetime import datetime

date1_str = "2025-02-20 10:00:00"
date2_str = "2025-02-21 10:00:00"

format = "%Y-%m-%d %H:%M:%S"

date1 = datetime.strptime(date1_str, format)
date2 = datetime.strptime(date2_str, format)

difference = abs((date2 - date1).total_seconds())

print(difference)

#86400.0