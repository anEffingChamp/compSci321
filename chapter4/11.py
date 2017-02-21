# Jonathan Smalls
# jon@smalls.rocks
# chapter 4.11 assignment
# find number of days in a month
import sys;
import math;
# A mathematician has published an arithmetic solution online. We just need to
# separately account for leap years. This is what Python gets for not having
# switch statements.
# https://cmcenroe.me/2014/12/05/days-in-month-formula.html
month = eval(input('Please input the integer value of an annual month: '))
year  = eval(input('Please input a four digit year: '));
# We calculate the month days according to the formula.
monthDays = 28 + (month + math.floor(month / 8)) % 2 + 2 % month + 2 * math.floor(1 / month);
# If the month is 2 for February, we also add a day for leap years. If the year
# is divisible by 4, add a leap day. If it is divisible by 100, but not 400, we
# can just remove that leap day.
if (2 == month and 0 == year % 4):
    monthDays = monthDays + 1;
    if (0 == year % 100 and 0 != year % 400):
        monthDays = monthDays - 1;
print('There are ' + str(monthDays) + ' days in this month');
