# (Turtle: draw a line) Write a program that draws a red line connecting two points (-39, 48) and (50, -50) and displays the coordinates of the two points, as shown in Figure 1.19b.
import turtle;
firstX  = -39;
firstY  = 48;
secondX = 50;
secondY = -50;

firstString  = "This position is: " + str(firstX) + ', ' +  str(firstY) + '.';
secondString = "This position is: " + str(secondX) + ', ' +  str(secondY) + '.';

turtle.hideturtle();
turtle.up();
turtle.goto(firstX, firstY);
turtle.write(firstString);
turtle.color('red');
turtle.down();
turtle.goto(secondX, secondY);
turtle.color('black');
turtle.write(secondString);
turtle.done();
