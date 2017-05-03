# Jonathan Smalls
# computer science 321
# 6.27: twin primes
import math
def isPrime(input):
    # If the loop executes to conclusion then the value must be a prime number.
    for loop in range(3, int(math.sqrt(input)), 2):
        if (0 == input % loop):
            return False
    return True

print('We will display all twin primes between 0, and 1000. Twin primes are defined as prime numbers that differ by two.')
for loop in range(1, 1000, 2):
    if (True == isPrime(loop) and True == isPrime(loop + 2)):
        print('(' + str(loop) + ', ' + str(loop + 2) + ')')
