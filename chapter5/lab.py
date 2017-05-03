# author Jonathan Smalls
# computer science 321
# Problem Description:
# (Conversion from kilograms to pounds and pounds to kilograms) Write a program
# that displays the following two tables side by side (note that 1 kilogram is
# 2.2 pounds and that 1 pound is .45 kilograms):
# Kilograms   Pounds      |      Pounds         Kilograms
# 1               2.2         |      20                 9.09
# 3               6.6            |      25                 11.36
# ...
# 197             433.4     |      510                231.82
# 199             437.8     |      515                235.09
print('Kilograms', end='\t')
print('Pounds', end='\t|\t')
print('Pounds', end='\t')
print('Kilograms')
pounds = 20
for loop in range(1, 200, 2):
    print(str(loop), end='\t')
    print(str(round(loop * 2.2, 1)), end='\t|\t')
    print(str(pounds), end='\t')
    print(str(round(pounds * 0.45, 2)))
    pounds += 5
