# Jonathan Smalls
# jon@smalls.rocks
# chapter 4.17 assignment
# rock paper scissors
import random;
import sys;
random.seed();
user    = eval(input('scissor (0), rock (1), paper (2): '));
program = random.randrange(0, 2);
if program > user or (0 == program and 2 == user):
    outcome = ' You lose.';
if user > program or (0 == user and 2 == program):
    outcome = ' You win.';
if user == program:
    outcome = ' You tie.';
if 0 == program:
    program = 'scissor';
elif 1 == program:
    program = 'rock';
else:
    program = 'paper';
if 0 == user:
    user = 'scissor';
elif 1 == user:
    user = 'rock';
else:
    user = 'paper';
output  = 'The computer is ' + str(program) + ', you are ' + str(user) + '.';
print(output + outcome);
