# find the number of years, and days from minutes
minutes = eval(input('Enter the number of minutes: '));
minutesToDays = 60 * 24;
years         = minutes // (365 * minutesToDays);
days          = (minutes - (years * 365 * minutesToDays)) // minutesToDays;
print(str(minutes) + ' minutes is approximately ' + str(years) + ' years and ' + str(days) + ' days.');
