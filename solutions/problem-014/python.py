def get_next_no_collatz_seq(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


longest_number = 0
longest_terms_count = 0


# this takes around 40 seconds
# some tricks for this: don't start with the 1 million and count down. That's gonna exhaust the process
# start small and keep track of the terms count in each iteration. For a certain number, if the terms count is greater,
# mark that as the longest number. Once it reaches one million, you will get the number with the longest terms
for i in range(1, 1000000):
    terms_count = 1
    temp = i

    while temp != 1:
        terms_count += 1
        if terms_count > longest_terms_count:
            longest_terms_count = terms_count
            longest_number = i
        temp = get_next_no_collatz_seq(temp)

print(longest_number)
