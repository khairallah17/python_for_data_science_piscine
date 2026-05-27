import time 
import datetime

current_time = time.time()
gmtime = time.gmtime()
x = datetime.datetime(gmtime.tm_year, gmtime.tm_mon, gmtime.tm_mday)
print("Seconds since January 1, 1970: {:,.3f} or {:.3} in scientific notation".format(current_time, current_time))
print(x.strftime("%b %d %Y"))
