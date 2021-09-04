from math import sqrt


def is_prime_number(number):
    # we only need to loop from 2 to square root of number
    # https://stackoverflow.com/a/5811176/4388776
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_nth_prime(n):
    count = 0
    number = 2
    while True:
        if is_prime_number(number):
            count = count + 1
            if count == n:
                return number
        number = number + 1


print(get_nth_prime(10001))