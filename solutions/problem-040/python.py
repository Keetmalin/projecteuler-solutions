# i am trying to do this in a brute force manner because I know my machine can handle a large string ;)
# generate the number until 1000000 digits
# there should be a nicer way to solve this number.
# To understand this concept, read: https://en.wikipedia.org/wiki/Champernowne_constant


def get_concat_of_numbers(limit):
    number = ""
    i = 1
    while len(number) < limit:
        number += str(i)
        i += 1
    return number


number = get_concat_of_numbers(1000000)
value = int(number[1 - 1]) * int(number[10 - 1]) * int(number[100 - 1]) * int(number[1000 - 1]) * int(number[10000 - 1]) \
        * int(number[100000 - 1]) * int(number[1000000 - 1])

print(value)
