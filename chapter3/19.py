# draw a line
firstX  = eval(input('Please input an integer for the first X coordinate: '));
firstY  = eval(input('Please input an integer for the first Y coordinate: '));
secondX = eval(input('Please input an integer for the second X coordinate: '));
secondY = eval(input('Please input an integer for the second Y coordinate: '));

import turtle;
turtle.hideturtle();
turtle.penup();
turtle.goto(firstX, firstY);
turtle.write('(' + str(firstX) + '), (' + str(firstY) + ')');
turtle.pendown();
turtle.goto(secondX, secondY);
turtle.write('(' + str(secondX) + '), (' + str(secondY) + ')');
turtle.done();
