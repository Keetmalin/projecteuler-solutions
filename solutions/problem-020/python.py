# This is a simple problem. We need to find the factorial first and then take the sum
# Here are the steps to do that.
# Consider the number 20.
# First we have to find the 20! . We can use the "math" module for that.
# 20! = 2432902008176640000
# Then we have 2 options to calculate the sum. 
# We can use integer operations (division and remainder) to separate numbers.
# But let's use string operations instead.
# We can convert 2432902008176640000 to a string using "str" function.
# Then we can convert "2432902008176640000" string to list of strings using "list" function.
# ['2', '4', '3', '2', '9', '0', '2', '0', '0', '8', '1', '7', '6', '6', '4', '0', '0', '0', '0']
# Then we can convert each string in above list to an integer using "map" function so that we get an integer list(map object).
# [2, 4, 3, 2, 9, 0, 2, 0, 0, 8, 1, 7, 6, 6, 4, 0, 0, 0, 0]
# Then we can use "sum" method to get the sum.
# I'll do all of the above steps with one line.

import math


def get_factorial_digit_sum(N):
    return sum(map(int, list(str(math.factorial(N)))))


print(get_factorial_digit_sum(100))
