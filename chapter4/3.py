# Jonathan Smalls
# jon@smalls.rocks
# chapter 4.3 assignment
# solve 2x2 linear equation
import sys;
valueA = eval(input('Please input a value for A: '));
valueB = eval(input('Please input a value for B: '));
valueC = eval(input('Please input a value for C: '));
valueD = eval(input('Please input a value for D: '));
valueE = eval(input('Please input a value for E: '));
valueF = eval(input('Please input a value for F: '));
finalDenominator = ((valueA * valueD) - (valueB * valueC));
# We can not divide by zero, so we have an error condition for such a
# denominator.
if (0 == finalDenominator):
    print('The equation has no solution.');
    sys.exit();
finalX = ((valueE * valueD) - (valueB * valueF)) / finalDenominator;
finalY = ((valueA * valueF) - (valueE * valueC)) / finalDenominator;
print('The value of X is ' + str(finalX));
print('The value of Y is ' + str(finalY));
