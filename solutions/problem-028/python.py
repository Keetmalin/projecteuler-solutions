# We can observe that one diagonal has the pattern of 1, 3, 7, 13, 21 and,
# the other diagonal contains the same values + some delta value
# Following algoriths calculates the sum using that delta value

def diagonal_sum(n):
    sum = 1 + ((n+1)%2)*2
    fn = 1
    for i in range(1, n):
        fn += 2*i
        sum += (2*fn) + (((i+(n%2))//2)*2) + ((n + 1)%2)
    return sum

# Tests
assert diagonal_sum(1) == 1
assert diagonal_sum(2) == 10
assert diagonal_sum(3) == 25
assert diagonal_sum(4) == 56
assert diagonal_sum(5) == 101

print(diagonal_sum(1001))
