from functools import reduce


# https://stackoverflow.com/a/6800214/4388776
def get_factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if not n % i)))


def check_triangle_factors_count_n(n):
    count = 1
    number = 1
    while True:
        factors = get_factors(number)
        if len(factors) > n:
            return number
        count += 1
        number += count


print(check_triangle_factors_count_n(500))
