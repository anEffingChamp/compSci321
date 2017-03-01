# Jonathan Smalls
# jon@smalls.rocks
# chapter 4.39 assignment
# draw two circles
import turtle;
import math;
firstX       = eval(input('Please input the first X coordinate: '));
firstY       = eval(input('Please input the first Y coordinate: '));
firstRadius  = eval(input('Please input the first radius: '));
secondX      = eval(input('Please input the second X coordinate: '));
secondY      = eval(input('Please input the second Y coordinate: '));
secondRadius = eval(input('Please input the second radius: '));
# We determine whether the circles nest, or overlap by calculating the slope to
# through their centers, and then determining where their edges intersect that
# line.
slope = (firstY - secondY) / (firstX - secondX);
# We check the crossings on the positive slope first.
firstEdge = '';
secondEdge = '';
firstCrossing = 'out';
if firstEdge >= secondEdge:
    firstCrossing = 'in';
# We then check the corssing on the negative slope.
firstEdge = '';
secondEdge = '';
secondCrossing = '';
if 'in' == firstCrossing and 'in' == secondCrossing:
    message = 'circle2 is inside of circle1';
elif 'out' == firstCrossing and 'out' == secondCrossing:
    message = 'circle2 is outside of circle1';
else:
    message = 'circle2 overlaps circle1';
# Then we draw the circles, and present the message.
turtle.hideturtle();
for point in [[firstX, firstY, firstRadius], [secondX, secondY, secondRadius]]:
    turtle.penup();
    turtle.goto(point[0], point[1]);
    turtle.pendown();
    turtle.circle(point[2]);
turtle.write(message);
turtle.done();
