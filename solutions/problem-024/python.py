# Following algorithm generates all permutations of a given string with given indexed order.
# So when we give "0123456789" as the initial string, it generates all permutations with alphabetical order
# Then out of all permutations, we can return the value in any position.


def get_permutations(S):
    if len(S) <= 1:
        return [S]
    permutations = []
    for s in S:
        for i in get_permutations(S.replace(s, "")):
            permutations += [s+i]
    return permutations


def get_N_th_permution(N):
    all_permutations = get_permutations("0123456789")
    return all_permutations[N-1]


N = 1000000
print(get_N_th_permution(N))
