# draw four tangential circles
import turtle;
turtle.hideturtle();
radius = eval(input('Please input a circle radius: '));
for loop in ([1, 1], [1, -1,], [-1, -1], [-1, 1]):
    turtle.penup();
    turtle.goto(radius * loop[0], radius * loop[1]);
    turtle.pendown();
    turtle.circle(radius);
turtle.done();
