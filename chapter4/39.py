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
# http://math.stackexchange.com/questions/9365/endpoint-of-a-line-knowing-slope-start-and-distance
slope          = (firstY - secondY) / (firstX - secondX);
cosine         = 1 / math.sqrt(1 + slope ** 2);
sine           = slope / math.sqrt(1 + slope ** 2);
centerDistance = math.sqrt((secondX - firstX) + (secondY - firstY));
firstEdgeX  = firstX + firstRadius * cosine;
firstEdgeY  = firstY + firstRadius * sine;
secondEdgeX = secondX + secondRadius * cosine;
secondEdgeY = secondY + secondRadius* sine;
if firstRadius >= secondRadius + centerDistance:
    message = 'circle2 is inside of circle1';
elif centerDistance >= firstRadius + secondRadius:
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
