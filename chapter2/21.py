# monthly savings calculation
savings      = eval(input('Please enter a monthly savings amount: '));
total        = 0;
interestRate = 1 + (0.05 / 12);
for loop in range(1, 7):
    total = round((total + savings) * interestRate, 2);
print('After the sixth month, the account value will be ' + str(total));
