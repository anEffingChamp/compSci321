# (Population projection) The US Census Bureau projects population based on the following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years. Assume the current population is 312032486 and one year has 365 days. Hint: in Python, you can use integer division operator // to perform division. The result is an integer. For
# example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).

populationBase = 312032486;
secondsInDay   = 60 * 60 * 24;
days           = 365;
for loop in range(0, 6):
    secondsElapsed = loop * secondsInDay * days;
    population = populationBase + (secondsElapsed // 7) + (secondsElapsed // 45) - (secondsElapsed // 13);
    print('The population at year ', loop, 'is ', population);
