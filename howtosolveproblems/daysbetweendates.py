# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     """
#      Calculates the number of days between two dates.
#     """
#     # TODO - by the end of this lesson you will have
#     #  completed this function. You do not need to complete
#     #  it yet though!

#     # TWO OPTIONS
#     # [1]
#     # from datetime import date
#     # date1 = date(year1, month1, day1)
#     # date2 = date(year2, month2, day2)
#     # delta = date2 - date1
#     # return delta.days

#     # [2]
#     if year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
#         return True
#     else:
#         return False


# def testDaysBetweenDates():

#     # test same day
#     assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
#     # test adjacent days
#     assert(daysBetweenDates(2017, 12, 30, 2017, 12, 31) == 1)
#     # test new year
#     assert(daysBetweenDates(2017, 12, 30, 2018, 1,  1) == 2)
#     # test full year difference
#     assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29) == 365)

#     print("Congratulations! Your daysBetweenDates")
#     print("function is working correctly!")


# testDaysBetweenDates()

###
# Define a simple nextDay procedure, that assumes
# every month has 30 days.
###
# For example:
# nextDay(1999, 12, 30) => (2000, 1, 1)
# nextDay(2013, 1, 30) => (2013, 2, 1)
# nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

###
# Define a simple nextDay procedure, that assumes
# every month has 30 days.
###
# For example:
# nextDay(1999, 12, 30) => (2000, 1, 1)
# nextDay(2013, 1, 30) => (2013, 2, 1)
# nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
     Returns the year, month, day of the next day.
     Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    start_date = [year, month, day]
    next_date = list()

    if start_date[1] <= 12 and start_date[2] < 30:
        next_date.append(year)
        next_date.append(start_date[1])
        next_date.append(start_date[2] + 1)
    elif start_date[1] < 12 and start_date[2] == 30:
        next_date.append(year)
        next_date.append(start_date[1] + 1)
        next_date.append(1)
    elif start_date[1] == 12 and start_date[2] == 30:
        year += 1
        next_date.append(year)
        next_date.append(1)
        next_date.append(1)

    print(tuple(next_date))


# nextDay(1999, 12, 30)
nextDay(2000, 1, 1)
# nextDay(2013, 1, 30)
nextDay(2013, 2, 1)
# nextDay(2012, 12, 30)
nextDay(2013, 1, 1)
nextDay(2012, 1, 1)
nextDay(2012, 4, 30)
nextDay(2012, 12, 1)
nextDay(1999, 12, 30)
nextDay(2012, 12, 30)
