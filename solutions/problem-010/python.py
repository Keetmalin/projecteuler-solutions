from math import sqrt


def is_prime_number(number):
    if number == 1:
        return False
    # we only need to loop from 2 to square root of number
    # https://stackoverflow.com/a/5811176/4388776
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def find_all_primes(limit):
    primes = []
    for i in range(1, limit):
        if is_prime_number(i):
            primes.append(i)
    return primes


primes = find_all_primes(2000000)
print(sum(primes))
