def find_sum_of_multiple_of_3_5(number):
    total = 0
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            total = total + n
    return total


total = find_sum_of_multiple_of_3_5(1000)
print(total)
