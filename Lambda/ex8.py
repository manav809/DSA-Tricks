import datetime

now = datetime.datetime.now()

print(now)

year = lambda x : x.year

month = lambda x: x.month

day = lambda x: x.day

time = lambda x: x.time()

print(year(now))
print(month(now))
print(day(now))
print(time(now))