days = int(input("Enter the number of days: "))
years = days // 365
months = (days % 365) // 30
remaining_days = (days % 365) % 30
print(f"{days} days is approximately {years} years, {months} months, and {remaining_days} days.")