# author Jonathan Smalls
# computer science 321
# display leap years in 21st century
count = 0
# 2100 will not be a leap year, so I can exclude that from the loop.
for year in range(2001, 2100):
    if (0 == year % 4):
        print(str(year), end='\t')
        count += 1
        if (10 == count):
            count = 0
            print()
