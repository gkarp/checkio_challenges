'''
Mission: Digits Multiplication
You are given a positive integer. Your function should calculate the product of
the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 
(don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.
'''
def checkio(number):
    number = str(number)
    sum = 1
    for digit in number:
        if digit != "0":
            sum *= int(digit)
    return sum