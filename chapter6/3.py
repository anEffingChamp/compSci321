# author Jonathan Smalls
# computer science 321
# palindrome integer
# return the reversal of an integer
def reverse(input):
    # https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    return input[::-1]

def isPalindrome(input):
    if (input == reverse(input)):
        print(input + ' is a palindrome')
        return
    print(input + ' is not a palindrome')

number = input('Please input an integer: ')
isPalindrome(number)
