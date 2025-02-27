#Write a Python program to drop microseconds from datetime.

import datetime

time = datetime.datetime.now()
no_mcsecs = time.replace(microsecond=0)

print(no_mcsecs)
#2025-02-27 23:45:34