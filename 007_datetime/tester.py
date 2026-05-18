# import time

# start = time.time()  # Unix Timestamp format (current date and time)

# print(time.ctime())

# local_time = time.localtime()

# print('Local', local_time.tm_wday)

# # time.sleep(4)

# stop = time.time()
# print(stop - start)

# import calendar

# cal = calendar.month(2026, 5, w=3, l=3)
# print(cal)

# cal = calendar.calendar(2026, w=2, l=1, c=10, m=4)
# print(cal)

# year_to_check = 1700

# print(calendar.isleap(year_to_check))
# print(calendar.leapdays(2000, 2024))

# print(calendar.weekday(2026, 5, 17))

# print(calendar.monthrange(2026, 5))
# print(calendar.MONDAY)

# import datetime

# my_birthday = datetime.date(1988, 3, 16)

# print(my_birthday)

# today = datetime.date.today()
# print(today)
# tdelta = today - my_birthday
# print(tdelta.total_seconds())
# tdelta = datetime.timedelta(15)
# print(today + tdelta)

# print(today.weekday())
# print(today.isoweekday())
# print(today.timetuple())


# date1 - date2 = timedelta
# date1 - timedelta = date2
# date2 + timedelta = date1

# t = datetime.time(19, 51, 25, 123134)
# t2 = datetime.time(8, 56, 16)


# dt = datetime.datetime(1988, 3, 16, 5, 30, 15)
# today = datetime.datetime.today()

# print(today - dt)

# tdelta = datetime.timedelta(0, 0, 0, 0, 0, 48)

# print(today.timestamp())
# ts = 1779124592.34375
# print(datetime.datetime.fromtimestamp(ts))

# today = datetime.datetime.now()

# print(type(today.strftime('%H-*-%M')))
# date_str = 'Monday 18/05/26 13:42'

# dt = datetime.datetime.strptime(date_str, '%A %d/%m/%y %H:%M')
# print(dt)

