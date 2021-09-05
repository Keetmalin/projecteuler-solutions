from math import sqrt


def find_pythagorean_triplet(limit):
    # a < b < c. So A can at most be less than limit//3
    # and a + b + c = limit
    for a in range(1, limit//3):
        # c = limit - a - b and b < c ==> b < limit - a - b ==> b < (limit - a)/2
        for b in range(a+1, (limit - a)//2):
            c = limit - a - b
            if a + b + c == limit and sqrt(a**2 + b**2) == c:
                return a * b * c


print(find_pythagorean_triplet(1000))