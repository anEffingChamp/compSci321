# reverse number
import sys
input = eval(input('Please enter a four digit number: '));
if (input < 1000):
    print('The string is not four characters long.');
    sys.exit();
digit4 = input // 1000;
digit3 = (input - (digit4 * 1000)) // 100;
digit2 = (input - (digit4 * 1000) - (digit3 * 100)) // 10;
digit1 = input - (digit4 * 1000) - (digit3 * 100) - (digit2 * 10);
print('The reversed number is ' + str(digit1) + str(digit2) + str(digit3) + str(digit4));
