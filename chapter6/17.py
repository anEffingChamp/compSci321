# Jonathan Smalls
# computer science 321
# 6.17 myTriangle module
# returns true if sum of any two sides is greater than third
import sys
import math
def isValid(side1, side2, side3):
    for side in [side1, side2, side3]:
        lengthsTemp = [side1, side2, side3]
        lengthsTemp.remove(side)
        if (sum(lengthsTemp) > side):
            continue
        return False

# returns area of triangle
def area(side1, side2, side3):
    # https://en.wikipedia.org/wiki/Triangle#Computing_the_area_of_a_triangle
    # We use Herons formula to calculate.
    areaSemi = (side1 + side2 + side3) / 2
    area = math.sqrt(areaSemi * (areaSemi - side1) * (areaSemi - side2) * (areaSemi - side3))
    print('The area of the triangle is ' + str(area))
    return

print('We will calculate the area of a triangle.')
sides = []
for loop in range(0, 3):
    side = eval(input('Please enter the length of side ' + str(loop + 1) + ': '))
    sides.append(side)

if False == isValid(sides[0], sides[1], sides[2]):
    print('These side lengths can not form a triangle.')
    sys.exit
area(sides[0], sides[1], sides[2])
