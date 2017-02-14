# reverse number
import sys
input = input('Please enter a four digit number: ');
if (len(input) != 4):
    print('The string is not four characters long.');
    sys.exit();
# TODO There is no reason to require an integer for this exercise. The program
# can reverse any four character string.
# https://docs.python.org/2/whatsnew/2.3.html#extended-slices
print('The reversed number is ' + input[::-1]);
