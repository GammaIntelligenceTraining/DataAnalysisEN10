import time
import calendar

# ==========================================
# 1. The 'time' Module
# ==========================================
print("--- 1. The 'time' Module ---")

# Epoch time: Seconds since January 1, 1970
seconds = time.time()
print(f"Seconds since epoch: {seconds}")

# Converting seconds to a readable string
local_time = time.ctime(seconds)
print(f"Local time (ctime): {local_time}")

# Getting a structured time object (struct_time)
struct_time = time.localtime()
print(f"Year from struct: {struct_time.tm_year}")
print(f"Month from struct: {struct_time.tm_mon}")

# time.sleep(): Pause execution
print("Sleeping for 1.5 seconds...")
time.sleep(1.5)
print("Done sleeping!\n")


# ==========================================
# 2. The 'calendar' Module
# ==========================================
print("--- 2. The 'calendar' Module ---")

# Printing a specific month
yy = 2026
mm = 5
print(f"Calendar for {calendar.month_name[mm]} {yy}:")
print(calendar.month(yy, mm))

# Checking for leap years
year_to_check = 2024
is_leap = calendar.isleap(year_to_check)
print(f"Is {year_to_check} a leap year? {is_leap}")

# Counting leap years in a range
leap_count = calendar.leapdays(2000, 2026)
print(f"Leap years between 2000 and 2026: {leap_count}")

# monthrange: Returns (first_day_weekday, number_of_days_in_month)
# Useful for iterating through all days of a month
first_day, num_days = calendar.monthrange(2026, 5)
print(f"May 2026 starts on weekday {first_day} and has {num_days} days.")

# Finding the weekday of a specific date
# 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
day_idx = calendar.weekday(2026, 5, 18)
print(f"Weekday index for 2026-05-18: {day_idx} ({calendar.day_name[day_idx]})")

# Textual calendar for the whole year (compact)
# print(calendar.calendar(2026)) 
