# This is a mathematical problem. What you need to find here is the least common multiple (LCM) of 1 through 20
# You can use a different approach, but it's gonna take a very long time
# https://math.stackexchange.com/a/328527/205151
# lcm(1,2,…,20)=2^4⋅3^2⋅5⋅7⋅11⋅13⋅17⋅19
from math import sqrt


def is_prime_number(number):
    # we only need to loop from 2 to square root of number
    # https://stackoverflow.com/a/5811176/4388776
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def find_max_power_limit(base, limit, power = 1):
    if base ** power > limit:
        return power - 1
    return find_max_power_limit(base, limit, power+1)


def find_smallest_multiple_until_limit(limit):
    lowest_multiple = 1
    for i in range(2, limit):
        if is_prime_number(i):
            max_power = find_max_power_limit(i, limit)
            lowest_multiple = lowest_multiple * (i ** max_power)
    return lowest_multiple


print(find_smallest_multiple_until_limit(20))
