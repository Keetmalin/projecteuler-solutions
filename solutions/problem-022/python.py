# First I remove all (") charactors and create a list of names by splitting the conent with comma.
# Then I sort ehe list and take the sum of name scores.


def get_names_from_file(filename):
    with open(filename, "r") as f:
        return f.read().replace("\"", "").split(",")


# "ord" function returns the (alphabetical value a charactor + 64), so we have to substract that total amount to get the value of the word
def get_alphabetical_value(word):
    return sum((map(ord, list(word)))) - (64 * len(word))


def get_sum_of_names_scores(filename):
    names = get_names_from_file(filename)
    names.sort()
    index = 1
    total = 0
    for name in names:
        total += index * get_alphabetical_value(name)
        index += 1
    return total


print(get_sum_of_names_scores("p022_names.txt"))
