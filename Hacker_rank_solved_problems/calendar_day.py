# Given a specific date in the format DD MM YYYY, determine
# and print the day of the week that date falls on.

import calendar
def day_of_year(day,month,year):
    # Split the input date into day, month, and year
    # Get the weekday for the given date
    weekday = calendar.weekday(year, month, day)
    print(calendar.day_name[weekday].upper())
    # Return the name of the weekday
    return calendar.day_name[weekday]

day_of_year(24,6,2005)
