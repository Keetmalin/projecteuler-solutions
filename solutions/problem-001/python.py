def find_sum_of_multiple_of_3_5(number):
    total = 0
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            total = total + n
    return total


total = find_sum_of_multiple_of_3_5(1000)
print(total)


#############################################
# A more faster method using math equations
# a = Initial number of the sequence = d = Gap between two numbers
# l = last number of the sequence
# n = number of items in the sequence
# S = sum of the sequence
# N = given upper limit
# Let's use the following equation of sum of a sequence
# Sn = n{2a + (n-1)d} / 2
# We know the a = d
# Also we can calculate:
# n = N // a
# Using all of that we can do a O(1) operation as follow.

def get_sum_until(N, a):
    n = N // a
    return (n * a * (1 + n)) // 2


def find_sum_of_multiple_of_3_5_second_method(number):
    # -1 is added because given upper limit should be larger than the last item of the sequence
    return get_sum_until(number - 1, 3) + get_sum_until(number-1, 5) - get_sum_until(number-1, 15)


total = find_sum_of_multiple_of_3_5_second_method(1000)
print(total)
