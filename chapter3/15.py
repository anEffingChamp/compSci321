# smiley face
import turtle
turtle.hideturtle();
# We draw the circle to house the face.
turtle.penup();
turtle.goto(0, -100);
turtle.pendown();
turtle.circle(100);
# We draw the smile.
for heading in (30, 150):
    turtle.penup();
    turtle.goto(0, -66);
    turtle.pendown();
    turtle.setheading(heading);
    turtle.forward(66);
# We draw the triangle nose.
turtle.penup();
turtle.goto(0, 30);
turtle.pendown();
# When drawing an equilateral triangle, the turtle first rotates 60 degrees
# before drawing the first line. We need to account for that by subtracting an
# appropriate number of degrees from our initial heading.
turtle.setheading(225 - 45);
turtle.circle(33, 360, 3);
# We draw the eyes.
for position in (30, -30):
    turtle.penup();
    turtle.goto(position, 60);
    turtle.pendown();
    turtle.dot(20, "black");

turtle.done();
