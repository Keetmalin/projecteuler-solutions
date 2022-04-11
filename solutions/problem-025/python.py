# We have to initialize first fibonacci couple - (1, 1)
# Then with each iteration we calculate next fibonacci couple.
# (1, 2) , (2, 3) , (3, 5) ... etc.
# We also keep the iteration count.
# When the required length reached, we return the iteration count.


def get_first_fibonacci_num_with_length(N):
    i_th_fibonacci_number = 1
    next_fibonacci_number = 1  # i+1 th fibonacci number
    count = 1
    while(len(str(i_th_fibonacci_number)) < N):
        i_th_fibonacci_number, next_fibonacci_number = next_fibonacci_number, next_fibonacci_number + i_th_fibonacci_number
        count += 1
    return count


print(get_first_fibonacci_num_with_length(1000))
