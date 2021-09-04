from math import sqrt
from functools import reduce

# if you are not smart enough, it might take a long time to process this

def is_prime_number(number):
    # we only need to loop from 2 to square root of number
    # https://stackoverflow.com/a/5811176/4388776
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# https://stackoverflow.com/a/6800214/4388776
def get_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))


def prime_factors(number):
    factors = get_factors(number)

    prime_factors = []
    for f in factors:
        if is_prime_number(f):
            prime_factors.append(f)
    return prime_factors


prime_factors = prime_factors(600851475143)

print(max(prime_factors))
