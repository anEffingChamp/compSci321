Exercise 6.29
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Return true if the card number is valid
def isValid(number):
        # print("isValid function")
            return getSize(number)>=13 and getSize(number)<=16 and \
                        (prefixMatched(number, 4) or prefixMatched(number, 5) or \
                            prefixMatched(number, 37) or prefixMatched(number, 6)) and \
                                (sumOfDoubleEvenPlace(number)+sumOfOddPlace(number))%10==0

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
        #print("sumOfDoubleEvenPlace")
            number =  number // 10
                sumOfEven = 0
                    while number!=0:
                                remainder = number % 10
                                        number //= 100
                                                remainder *= 2
                                                        if remainder>=10:
                                                                        remainder = getDigit(remainder)
                                                                                print(remainder)
                                                                                        sumOfEven += remainder
                                                                                            return sumOfEven
# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
                                                                                            def getDigit(number):
                                                                                                    #print("getDigit")
                                                                                                        return number%10 + number//10

# Return sum of odd place digits in number
def sumOfOddPlace(number):
        #print("sumOfOddPlace")
            sumOfOdd = 0
                while number!=0:
                            remainder = number % 10
                                    number //= 100
                                            #print(remainder)
                                                    sumOfOdd += remainder
                                                        return sumOfOdd

# Return true if the digit d is a prefix for number
                                                       def prefixMatched(number, d):
                                                               return getPrefix(number, getSize(d))

# Return the number of digits in d
def getSize(d):
        #print("getSize")
            numberOfDigits = 0
                while d!=0:
                            d = d // 10
                                    numberOfDigits += 1
                                        return numberOfDigits

# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
        #print("getPrefix")
            result = number
                for i in range(getSize(number)-k):
                            result //= 10
                                return result

                            def main():
                                    creditNumber = eval(input("Please enter credit card number:"))
                                        if isValid(creditNumber):
                                                    print(creditNumber, " is valid!")
                                                        else:
                                                                    print(creditNumber, " is invalid!")

                                                                            main()
