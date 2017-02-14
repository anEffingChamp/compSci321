# character from ASCII code
import sys
code = eval(input('Please enter an ASCII code between 0, and 127: '));
if (code < 0 or code > 128):
    print('This input is not in the valid range.');
    sys.exit();
# TODO chr() returns empty spaces for low digit numbers. Is this normal?
print('The character is ' + chr(code));
