# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# 1 year 365 days
# 1 year 52 weeks
# 1 year 12 months

age_int = int(age)

left_years = 90 - age_int
left_days = left_years * 365
left_weeks = left_years * 52
left_months = left_years * 12

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")
