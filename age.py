from datetime import datetime, date

user_date = input("Enter a date (in the format DD-MM-YYYY): ")
user_date = datetime.strptime(user_date, "%d-%m-%Y")

today = date.today()

age = today.year - user_date.year

if (today.month, today.day) < (user_date.month, user_date.day):
    age -= 1

print(f"The number of years from your date to now is {age} years.")
