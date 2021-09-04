def fibonacci_sequence(limit, numbers=None):
    if numbers is None:
        numbers = []
    if len(numbers) == 0:
        numbers.append(1)
        numbers.append(2)

    if numbers[-1] > limit:
        return numbers

    numbers.append(numbers[-1] + numbers[-2])
    return fibonacci_sequence(limit, numbers)


sequence = fibonacci_sequence(4000000)
total = sum(num for num in sequence if not num % 2)
print(total)
