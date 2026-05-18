import datetime
import calendar

"""
PYTHON DATETIME HOMEWORK
------------------------
Instructions: Complete the functions below. 
Do not use classes. Use the datetime, time, and calendar modules.
"""

# TASK 1: Age in Days
# Write a function that takes a birth date (year, month, day) 
# and returns the total number of days the person has lived until today.
def calculate_age_in_days(year, month, day):
    # Your code here
    pass

# TASK 2: The Next Friday the 13th
# Write a function that finds the date of the very next "Friday the 13th"
# starting from a given date (defaults to today).
def find_next_friday_13th(start_date=None):
    if start_date is None:
        start_date = datetime.date.today()
    # Your code here
    pass

# TASK 3: Weekend Counter
# Write a function that takes a year and a month and returns 
# the count of Saturdays and Sundays in that month.
def count_weekends(year, month):
    # Your code here
    pass

# TASK 4: Simple Countdown
# Write a function that takes a target datetime object and 
# prints a message every second until the time is reached.
# Use time.sleep(1).
def start_countdown(target_datetime):
    # Your code here
    pass


# --- TEST AREA (Optional: Use this to check your work) ---
if __name__ == "__main__":
    print("--- Homework Tests ---")
    
    # Example Test for Task 1
    # print(f"Days lived: {calculate_age_in_days(2000, 1, 1)}")
    
    # Example Test for Task 2
    # print(f"Next Friday 13th: {find_next_friday_13th()}")
    
    # Example Test for Task 3
    # print(f"Weekends in May 2026: {count_weekends(2026, 5)}")
