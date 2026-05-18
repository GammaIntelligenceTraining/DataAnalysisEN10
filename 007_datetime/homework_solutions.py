import datetime
import calendar
import time

# ==========================================
# SOLUTIONS FOR HOMEWORK.PY
# ==========================================

def calculate_age_in_days(year, month, day):
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    delta = today - birth_date
    return delta.days

def find_next_friday_13th(start_date=None):
    if start_date is None:
        current = datetime.date.today()
    else:
        current = start_date

    while True:
        # Check if today is the 13th and a Friday (4)
        if current.day == 13 and current.weekday() == 4:
            return current
        current += datetime.timedelta(days=1)

def count_weekends(year, month):
    weekends = 0
    # monthrange returns (first_day_weekday, number_of_days_in_month)
    _, num_days = calendar.monthrange(year, month)
    
    for day in range(1, num_days + 1):
        dt = datetime.date(year, month, day)
        if dt.weekday() >= 5: # 5 is Saturday, 6 is Sunday
            weekends += 1
    return weekends

def start_countdown(seconds):
    print(f"Starting countdown for {seconds} seconds...")
    while seconds > 0:
        print(f"T-minus: {seconds}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nLiftoff! 🚀")

# --- Example Usage ---
if __name__ == "__main__":
    print(f"Task 1: Days lived since 2000-01-01: {calculate_age_in_days(2000, 1, 1)}")
    print(f"Task 2: Next Friday the 13th: {find_next_friday_13th()}")
    print(f"Task 3: Weekends in May 2026: {count_weekends(2026, 5)}")
    # start_countdown(5) # Uncomment to test
