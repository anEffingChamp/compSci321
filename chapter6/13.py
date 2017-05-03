# Jonathan Smalls
# computer science 321
# 6.13: sum series
print('We will sum a series of fractions between 1/2 and i / i + 1')
input = eval(input('Please enter an integer greater than one: '))
print('count', end='\t')
print('m(count)')

sum = 0
for loop in range(1, input + 1):
    sum += loop / (loop + 1)
    print(loop, end='\t')
    print(round(sum, 4))
