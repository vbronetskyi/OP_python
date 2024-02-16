import calendar

def semester_calendar(output_type, year, first_month, last_month):
    """
    (str, int, int, int) -> str
    Precondition: first_month <= 12 and last_month <= 12 and first_month <= last_month
    Precondition: output_type == 'txt' or output_type == 'html'

    Returns the academic semester calendar in txt and html format

    >>> semester_calendar('txt', 2003, 9, 10)
    '   September 2003\\nMo Tu We Th Fr Sa Su\\n 1  2  3  4  5  6  7\\n 8  9 10 11 12 13 14\\n15 16 17 18 19 20 21\\n22 23 24 25 26 27 28\\n29 30\\n    October 2003\\nMo Tu We Th Fr Sa Su\\n       1  2  3  4  5\\n 6  7  8  9 10 11 12\\n13 14 15 16 17 18 19\\n20 21 22 23 24 25 26\\n27 28 29 30 31\\n'
    >>> semester_calendar("txt", 2021, 10, 10)
    '    October 2021\\nMo Tu We Th Fr Sa Su\\n             1  2  3\\n 4  5  6  7  8  9 10\\n11 12 13 14 15 16 17\\n18 19 20 21 22 23 24\\n25 26 27 28 29 30 31\\n'
    """
    if output_type == 'txt':
        output_type = ''
        c = calendar.TextCalendar()
        for i in range(first_month, last_month + 1):
            output_type += c.formatmonth(year, i)
    elif output_type == 'html':
        output_type = ''
        c = calendar.HTMLCalendar()
        for i in range(first_month, last_month + 1):
            output_type += c.formatmonth(year, i)

    return output_type
