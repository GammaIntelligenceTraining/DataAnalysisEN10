import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

# ==========================================
# 2. Working with Date and Time Objects
# ==========================================
print("--- 2. Working with Date and Time Objects ---")

# Creating a date object (Year, Month, Day)
my_birthday = datetime.date(1995, 5, 20)
print(f"Birthday: {my_birthday}")
print(f"Year: {my_birthday.year}, Month: {my_birthday.month}, Day: {my_birthday.day}")

# Today's date
today = datetime.date.today()
print(f"Today: {today}")

# Creating a time object (Hour, Minute, Second)
class_time = datetime.time(14, 30, 0)
print(f"Class starts at: {class_time}")

# Creating a datetime object (Date + Time)
now = datetime.datetime.now()
print(f"Current datetime: {now}")

# Combining date and time
combined = datetime.datetime.combine(today, class_time)
print(f"Combined: {combined}")
print("\n")


# ==========================================
# 3. Timedelta and Arithmetic
# ==========================================
print("--- 3. Timedelta and Arithmetic ---")

# Creating a duration (10 days, 5 hours)
delta = datetime.timedelta(days=10, hours=5)
print(f"Timedelta: {delta}")

# Adding duration to current time
future_date = today + datetime.timedelta(days=100)
print(f"100 days from today: {future_date}")

# Calculating difference between two dates
new_years = datetime.date(2027, 1, 1)
days_until_ny = new_years - today
print(f"Days until New Year 2027: {days_until_ny.days} days")

# Difference in seconds
one_hour_ago = now - datetime.timedelta(hours=1)
diff = now - one_hour_ago
print(f"Difference in seconds: {diff.total_seconds()}")
print("\n")


# ==========================================
# 4. Formatting and Parsing
# ==========================================
print("--- 4. Formatting and Parsing ---")

# strftime: Datetime to String
formatted = now.strftime("%A, %B %d, %Y - %H:%M:%S")
print(f"Formatted: {formatted}")

# strptime: String to Datetime
date_str = "27 October, 2023"
parsed_date = datetime.datetime.strptime(date_str, "%d %B, %Y")
print(f"Parsed from string: {parsed_date}")

# ISO Format (Standard)
iso_str = now.isoformat()
print(f"ISO Format: {iso_str}")
back_from_iso = datetime.datetime.fromisoformat(iso_str)
print("\n")


# ==========================================
# 5. Timezones and Localization
# ==========================================
print("--- 5. Timezones and Localization ---")

# Naive datetime (no timezone)
naive_now = datetime.datetime.now()
print(f"Naive: {naive_now.tzinfo}") # Returns None

# Aware datetime (with UTC)
utc_now = datetime.datetime.now(ZoneInfo("UTC"))
print(f"UTC Aware: {utc_now}")

# Converting to another timezone
tokyo_now = utc_now.astimezone(ZoneInfo("Asia/Tokyo"))
print(f"Tokyo Time: {tokyo_now}")

# Converting to New York time
ny_now = utc_now.astimezone(ZoneInfo("America/New_York"))
print(f"New York Time: {ny_now}")
print("\n")


# ==========================================
# 6. Real-World Application: Simple Log Parser
# ==========================================
print("--- 6. Lab: Simple Log Parser ---")

log_entries = [
    "2023-10-27 10:00:01 - User Login",
    "2023-10-27 10:05:20 - User Logout"
]

def calculate_session(logs):
    # Extracting timestamps
    login_str = logs[0].split(" - ")[0]
    logout_str = logs[1].split(" - ")[0]
    
    # Parsing
    fmt = "%Y-%m-%d %H:%M:%S"
    login_dt = datetime.datetime.strptime(login_str, fmt)
    logout_dt = datetime.datetime.strptime(logout_str, fmt)
    
    # Calculation
    duration = logout_dt - login_dt
    return duration.total_seconds()

seconds = calculate_session(log_entries)
print(f"Session lasted: {seconds} seconds")
print("\n")


# ==========================================
# 7. Interesting Use Cases & Patterns
# ==========================================
print("--- 7. Interesting Use Cases ---")

# --- Use Case A: Relative Time ("Time Ago") ---
def time_ago(dt):
    diff = datetime.datetime.now() - dt
    
    if diff.total_seconds() < 60:
        return "Just now"
    if diff.total_seconds() < 3600:
        return f"{int(diff.total_seconds() // 60)} minutes ago"
    if diff.days == 0:
        return f"{int(diff.total_seconds() // 3600)} hours ago"
    return f"{diff.days} days ago"

# Test relative time
post_date = datetime.datetime.now() - datetime.timedelta(minutes=45)
print(f"Post was created: {time_ago(post_date)}")


# --- Use Case B: Working Days (Excluding Weekends) ---
def count_business_days(start_date, end_date):
    days = 0
    current = start_date
    while current <= end_date:
        if current.weekday() < 5:  # 0-4 are Mon-Fri
            days += 1
        current += datetime.timedelta(days=1)
    return days

start = datetime.date(2023, 10, 23) # Monday
end = datetime.date(2023, 10, 30)   # Next Monday
print(f"Business days between {start} and {end}: {count_business_days(start, end)}")


# --- Use Case C: Finding "Next Friday" ---
def get_next_weekday(start_dt, weekday_idx):
    # weekday_idx: 0=Mon, 1=Tue, ..., 4=Fri, etc.
    days_ahead = weekday_idx - start_dt.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return start_dt + datetime.timedelta(days=days_ahead)

today_dt = datetime.datetime.now()
next_friday = get_next_weekday(today_dt, 4)
print(f"Next Friday will be: {next_friday.strftime('%Y-%m-%d')}")
