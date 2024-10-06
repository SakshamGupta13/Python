from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)

    # Calculate age in years, months, and days
    age_in_years = today.year - birth_date.year
    age_in_months = today.month - birth_date.month
    age_in_days = today.day - birth_date.day

    # Adjust if birth month/day has not yet occurred this year
    if age_in_days < 0:
        age_in_months -= 1
        age_in_days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

    if age_in_months < 0:
        age_in_years -= 1
        age_in_months += 12

    return age_in_years, age_in_months, age_in_days

# Input example
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

age_years, age_months, age_days = calculate_age(birth_year, birth_month, birth_day)
print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")