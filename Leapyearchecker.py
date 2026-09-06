year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# year is a leap year if it is divisible by 4 but not divisible by 100, or if it is divisible by 400.