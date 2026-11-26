day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

leap_year = False
valid_date = False

if year > 0 and month >= 1 and month <= 12:

    if year % 400 == 0:
        leap_year = True

    elif year % 100 == 0:
        leap_year = False

    elif year % 4 == 0:
        leap_year = True

    else:
        leap_year = False

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days_in_month = 31

    elif month == 4 or month == 6 or month == 9 or month == 11:
        days_in_month = 30

    elif month == 2:
        if leap_year:
            days_in_month = 29
        else:
            days_in_month = 28

    if day >= 1 and day <= days_in_month:
        valid_date = True

if leap_year:
    print("Leap Year: Yes")
else:
    print("Leap Year: No")

if valid_date:
    print("Date:", day, "/", month, "/", year)
    print("Valid Date: Yes")
else:
    print("Valid Date: No")
