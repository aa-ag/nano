# TWO OPTIONS
# [1]
#
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     """
#      Calculates the number of days between two dates.
#     """
#     # TODO - by the end of this lesson you will have
#     #  completed this function. You do not need to complete
#     #  it yet though!
#     # from datetime import date
#     # date1 = date(year1, month1, day1)
#     # date2 = date(year2, month2, day2)
#     # delta = date2 - date1
#     # return delta.days


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # YOUR CODE HERE!
    # PSEUDO CODE
    print([year2 - year1, month2 - month1, (day2 - day1) + 1])


def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()
