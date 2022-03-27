# The easiest way to get the reccurring cycle is to do the division using a pen and paper.
# So lets use that method and iteratively calculate the integer division and remainder.
# If we see the same pair (divided answer, remainder) again that means we are going to a cycle.

def get_recurring_cycle_length(p, q):
    mydict = {}
    i = 0
    while True:
        d = p*10//q
        p = (p*10) % q
        if p == 0:
            return 0
        pair = (d, p)
        if pair not in mydict:
            mydict[pair] = i
            i += 1
        else:
            return (i-mydict[pair])


def get_d_with_longest_recurring_cycle(n):
    max_length = 0
    d = 0
    for i in range(2, n):
        length = get_recurring_cycle_length(1, i)
        if length > max_length:
            max_length = length
            d = i
    return d


print(get_d_with_longest_recurring_cycle(1000))