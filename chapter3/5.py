# area of a regular polygon
import math;
sideCount  = eval(input('Please enter the number of sides: '));
sideLength = eval(input('Please enter the length of the sides: '));
area       = (sideCount * (sideLength ** 2)) / (4 * math.tan(math.pi / sideCount));
print('The area of the polygon is ' + str(area));
