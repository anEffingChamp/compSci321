# four digit integer displays numbers in reverse order
string = input('Please input a four digit number: ');
# I could validate that the number is four digits long, but that is not
# directly relevant to the loop, or assignment.
for loop in reversed(range(0, len(string))):
    print(string[loop]);
