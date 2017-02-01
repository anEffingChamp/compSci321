# Exercise 1.21
# (Turtle: display a clock) Write a program that displays a clock to show the time 9:15:00, as shown in Figure 1.20c.
import turtle;
turtle.hideturtle();
# We draw the circle to simulate the clock face. We want to use the origin as
# circle center, so we must move the turtle.
turtle.up();
turtle.goto(0, -100);
turtle.down();
turtle.circle(100);
# Then we draw the hour, and minute hands. The hour hand is 66% the length of
# the minute hand, but also twice as wide. The minute hand is 80% the radius of
# the full circle.
handLength = 80;
handWidth  = turtle.pensize();
turtle.up();
turtle.home();
turtle.down();
turtle.forward(handLength);
turtle.home();
turtle.left(180);
turtle.pensize(handWidth * 2);
turtle.forward(handLength * 0.66);
turtle.pensize(handWidth);
# Now we just have to print the time ordinals to the clock face.
for loop in range(3, 15, 3):
    turtle.up();
    turtle.home();
    turtle.right(90 * (loop - 3) / 3);
    turtle.forward(90);
    turtle.down();
    turtle.write(str(loop));

turtle.done();
