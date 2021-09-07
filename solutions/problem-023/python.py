# First I create a map of all abundant numbers. That is to increase the performance.
# Eveything else is self-explanatory.
# We will use the given 28123 as the upper limit.


def is_abundant(N):
    total = 0
    for i in range(1, N):
        if N % i == 0:
            total += i
    return N < total


def get_is_abundant_map(N):
    abundants = {}
    for i in range(1, N):
        abundants[i] = is_abundant(i)
    return abundants


def is_a_sum_of_two_abundant_numbers(N, abundants):
    for i in range(1, (N//2) + 1):
        if (abundants[i] and abundants[N-i]):
            return True
    return False


def get_sum_of_all_non_abundant_sums(N):
    abundants = get_is_abundant_map(N)
    total = 0
    for i in range(1, N):
        if not is_a_sum_of_two_abundant_numbers(i, abundants):
            total += i
    return total


print(get_sum_of_all_non_abundant_sums(28123))
