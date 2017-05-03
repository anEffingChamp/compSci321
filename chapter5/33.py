# author Jonathan Smalls
# computer science 321
# compute value of CD
amount     = eval(input('Please enter an initial deposit amount: '))
percentage = eval(input('Please enter the annual percentage yield: '))
period     = eval(input('Please enter the maturity period in months: '))

print('Month', end='\t')
print('Value')
for month in range(1, period + 1):
    print(month, end='\t')
    amount = round(amount + (amount * percentage / 1200), 2)
    print(amount)
