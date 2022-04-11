# Function names are self explanatory

import math


def is_prime(N):
    if N < 2:
        return False
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True


def evaluate_function(a, b, n):
    return (n*n) + (a*n) + b


def get_how_many_conecutive_primes(a, b):
    count = 0
    for n in range(0, b):  # When n = b, it is divisible by b
        if is_prime(evaluate_function(a, b, n)):
            count += 1
        else:
            break
    return count


def get_quadratic_primes(A, B):
    max_a = -A  # Assume the answer is greater than -A
    max_b = -(B+1)  # Assume the answer is greater than -(B+1)
    max_consecutive_prime_count = 0
    for a in range(-A + 1, A):
        for b in range(-B, B + 1):
            consecutive_prime_count = get_how_many_conecutive_primes(a, b)
            if consecutive_prime_count > max_consecutive_prime_count:  # Assume only one solution
                max_a = a
                max_b = b
                max_consecutive_prime_count = consecutive_prime_count
    return max_a * max_b


print(get_quadratic_primes(1000, 1000))
