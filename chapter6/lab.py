# Jonathan Smalls
# computer science 321
# Lab 6-1: Computing Future Investment Value

# Problem Description:
# Write a fuunction that computes future investment value at a given interest
# rate for a specified number of years. The future investment is determined
# using the following formula:
# futureInvestmentValue = investmentAmount x (1 + monthlyInterestRate)numberOfYears*12

# Use the following function header:
# def futureInvestmentValue(investmentAmount, monthlyInterestRate, years)
# For example, futureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.
# Write a test program that prompts the user to enter the investment amount (e.g., 1000) and the interest rate (e.g., 9%) and prints a table that displays future value for the years from 1 to 30, as shown below:

# The amount invested: 1000
# Annual interest rate: 9%
# Years        Future Value
# 1             1093.80
# 2             1196.41
# ...
# 29            13467.25
# 30            14730.57
print('This program will calculate investment appreciation over a number of years')
deposit = eval(input('Please input an initial investment value: '))
rate    = eval(input('Please input an interest rate: '))
period  = eval(input('Please input an investment period in years: '))

print('The amount invested: ' + str(deposit))
print('Annual interest rate: ' + str(rate) + '%')
print('Years', end='\t')
print('Future Value')

rate = 1 + (rate / 100)
for year in range(0, period + 1):
    for month in range(1, 12 + 1):
        deposit = round(deposit + (deposit * rate / 1200), 2)
    print(str(year), end='\t')
    print(deposit)
