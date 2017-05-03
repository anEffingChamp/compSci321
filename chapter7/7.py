# Jonathan Smalls
# computer science 321
# 7.7: algebra 2x2 linear equations
import sys
class LinearEquation(object):
    def __init__(self, a, b, c, d, e, f):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def getA(self):
        return self._a

    def getB(self):
        return self._b

    def getC(self):
        return self._c

    def getD(self):
        return self._d

    def getE(self):
        return self._e

    def getF(self):
        return self._f

    def isSolvable(self):
        if (0 <= (self._a * self._d) - (self._b * self._c)):
            return True
        return False

    def getX(self):
        value = ((self._e * self._d) - (self._b * self._f)) / (self._a * self._d) - (self._b * self._c)
        return value

    def getY(self):
        value = ((self._a * self._f) - (self._e * self._c)) / (self._a * self._d) - (self._b * self._c)
        return value

print('This program will calculate solutions to linear algrebraic equations.')
inputA   = eval(input('Please enter a value for A: '))
inputB   = eval(input('Please enter a value for B: '))
inputC   = eval(input('Please enter a value for C: '))
inputD   = eval(input('Please enter a value for D: '))
inputE   = eval(input('Please enter a value for E: '))
inputF   = eval(input('Please enter a value for F: '))

equation = LinearEquation(inputA, inputB, inputC, inputD, inputE, inputF)
if (True == equation.isSolvable()):
    valueX = equation.getX()
    valueY = equation.getY()
    print('The value of X is ' + str(valueX))
    print('The value of Y is ' + str(valueY))
    sys.exit
print('The equation has no solution')
