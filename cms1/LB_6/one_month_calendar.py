"""Lab 6, ex 8"""
import calendar as Calendar

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> print(weekday_name(3))
    thu
    """
    week_day = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return week_day[number]

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    date = date.split('.')
    return Calendar.weekday(int(date[2]), int(date[1]), int(date[0]))

def calendar(month_: int, year_: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    calend = Calendar.TextCalendar().formatmonth(year_, month_, 3).split('\n')[2:]
    calend.insert(0, 'mon tue wed thu fri sat sun')
    calend = '\n'.join(calend)
    calend = calend[:-1]
    return calend

def transform_calendar(calendar: str) -> str:
    """
    Return a modified horizontal -> vertical calendar.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    """
    calendar = calendar.split('\n')
    for i in range(len(calendar)):
        calendar[i] = calendar[i].split(' ')
    
    lst = [[], [], [], [], [], [], []]
    for i in range(7):
        for j in range(7):
            lst[i].append(0)
    

    
    return calendar
print(transform_calendar(calendar(5, 2002)))
"""if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year))
    except ValueError as err:
        print(err)"""
