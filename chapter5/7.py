# author Jonathan Smalls
# computer science 321
# trigonometric functions
import math
print('Degrees', end='\t')
print('Sine', end='\t')
print('Cosine')
for angle in range(0, 360+1, 10):
    print(angle, end='\t')

    radians = math.radians(angle)
    print(round(math.sin(radians), 4), end='\t')
    print(round(math.cos(radians), 4))
