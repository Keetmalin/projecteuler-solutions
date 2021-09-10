# Simply append all numbers to a list and convet it into a set to get only distinct items

def get_distinct_num_count(start, end):
    new_list = []
    for a in range(start, end + 1):
        for b in range(start, end + 1):
            new_list.append(a ** b)
    return len(set(new_list))


print(get_distinct_num_count(2, 100))
