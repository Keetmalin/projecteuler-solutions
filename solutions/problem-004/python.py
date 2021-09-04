from functools import reduce


def is_palindrome(number):
    strNumber = str(number)
    for i in range(len(strNumber)//2):
        if strNumber[i] != strNumber[-i-1]:
            return False
    return True


# https://stackoverflow.com/a/6800214/4388776
def get_factors(number):
    return set(reduce(list.__add__, ([i, number//i] for i in range(1, int(number**0.5) + 1) if not number % i)))


def find_largest_palindrome_with_multiples(limit, n):
    for i in range(1, limit):
        number = limit - i
        if is_palindrome(number):
            factors = get_factors(number)
            for f in factors:
                if len(str(f)) == n and len(str(number // f)) == n:
                    return number


print(find_largest_palindrome_with_multiples(1000000, 3))
