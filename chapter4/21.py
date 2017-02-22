# Jonathan Smalls
# jon@smalls.rocks
# chapter 4.21 assignment
# day of the week
import math;
year          = eval(input('Please input a four digit year: '));
month         = eval(input('Please input a two digit month: '));
day           = eval(input('Please input a day of the month: '));
yearOfCentury = year % 100;
yearCentury   = year // 100;
# https://en.wikipedia.org/wiki/Zeller's_congruence
# This seems to be a fusion of the Julian, and Gregorian values on Wikipedia. I
# can not get an accurate day of the week with this formula, although it returns
# values. I have modified the formula, and used Friday = 0 to get the correct
# value for Wednesday, February 22, 2017.
dayOfWeek     = (day + math.floor(13 * (month + 1) / 5) + yearOfCentury + math.floor(yearOfCentury / 4) + math.floor(yearCentury / 4) + 5 - yearCentury) % 7;
if 0 == dayOfWeek:
    dayOfWeek = 'Friday';
elif 1 == dayOfWeek:
    dayOfWeek = 'Saturday';
elif 2 == dayOfWeek:
    dayOfWeek = 'Sunday';
elif 3 == dayOfWeek:
    dayOfWeek = 'Monday';
elif 4 == dayOfWeek:
    dayOfWeek = 'Tuesday';
elif 5 == dayOfWeek:
    dayOfWeek = 'Wednesday';
else:
    dayOfWeek = 'Thursday';
print('The day of the week is ' + dayOfWeek);
