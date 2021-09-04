def get_sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total = total + n ** 2
    return total


def get_square_of_sum(numbers):
    total = sum(numbers)
    return total ** 2


limit = 100
numList = [i for i in range(1, limit + 1)]
print(get_square_of_sum(numList) - get_sum_of_squares(numList))
