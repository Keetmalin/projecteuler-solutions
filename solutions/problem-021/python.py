# Here I've impelemented two helper methods and three algorithms to get the answer.
# Performance of following algorithms are as follows.
# get_sum_of_all_amicalbles_under_1 < get_sum_of_all_amicalbles_under_2 < get_sum_of_all_amicalbles_under_3
# (bad < good)

def get_sum_of_all_proper_divisors(N):
    total = 0
    for i in range(1, N):
        if N % i == 0:
            total += i
    return total


def is_amicable(N):
    a = get_sum_of_all_proper_divisors(N)
    b = get_sum_of_all_proper_divisors(a)
    return (N == b) and (a != b)


# Method 1
def get_sum_of_all_amicalbles_under_1(N):
    amicable_numbers = []
    for i in range(1, N):
        if i not in amicable_numbers:
            if(is_amicable(i)):
                amicable_numbers += [i]
    return sum(amicable_numbers)


# Method 2
def get_sum_of_all_amicalbles_under_2(N):
    amicable_numbers = []
    for i in range(1, N):
        if i not in amicable_numbers:
            if(is_amicable(i)):
                amicable_numbers += [i]
                b = get_sum_of_all_proper_divisors(i)
                if(b < N and b != i):
                    amicable_numbers += [b]
    return sum(amicable_numbers)


# Method 3
def get_sum_of_all_amicalbles_under_3(N):
    amicable_numbers = []
    total = 0
    for i in range(1, N):
        if i not in amicable_numbers:
            a = get_sum_of_all_proper_divisors(i)
            if a == i:
                continue  # Not amicable
            b = get_sum_of_all_proper_divisors(a)
            if(i == b):  # Amicable
                amicable_numbers += [i]
                total += i
                if(a < N and a != i):
                    amicable_numbers += [a]
                    total += a
    return total


N = 10000
print(get_sum_of_all_amicalbles_under_1(N))
# print(get_sum_of_all_amicalbles_under_2(N))
# print(get_sum_of_all_amicalbles_under_3(N))
