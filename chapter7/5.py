# Jonathan Smalls
# computer science 321
# 7.5: regular sided polygon
import math
class RegularPolygon(object):
    def __init__(self, sides = 3, length = 1, x = 0, y = 0):
        self._n    = int(sides)
        self._side = float(length)
        self._x    = float(x)
        self._y    = float(y)

    def getPerimeter(self):
        return self._n * self._side

    def getArea(self):
        area = (self._n * (self._side ** 2)) / (4 * math.tan(math.pi / self._n))
        return area

shapeA = RegularPolygon()
shapeB = RegularPolygon(6, 4)
shapeC = RegularPolygon(10, 4, 5.6, 7.8)
for shape in [shapeA, shapeB, shapeC]:
    print('The perimeter for this shape is ' + str(shape.getPerimeter()))
    print('The area for this shape is ' + str(shape.getArea()))
