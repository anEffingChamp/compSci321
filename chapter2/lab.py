# Lab: Calculating Future Investment Value
# Problem Description:

# Write a program that reads in investment amount, annual interest rate, and number of years, and displays the future investment value using the following formula:
# and displays the future investment value using the following formula:

# futureInvestmentValue =
# investmentAmount * (1 + monthlyInterestRate)numberOfYears*12

# For example, if you enter amount 1000, annual interest rate 3.25%, and number of years 1, the future investment value is 1032.98.

# Hint: Use the Math.pow(a, b) method or ** operator to compute a raised to the power of b.

# Here is a sample run:

# Sample 1:
# Enter investment amount: 1000
# Enter annual interest rate: 4.25
# Enter number of years: 1
# Accumulated value is 1043.34
import math;
initial  = eval(input('Please enter investment amount: '));
interest = eval(input('Please enter annual interest rate: ')) / 100;
period   = eval(input('Please enter investment period in years: '));
final    = round(initial * (1 + (interest / 12)) ** (period * 12), 2);

print('The accumulated account value is ' + str(final));
