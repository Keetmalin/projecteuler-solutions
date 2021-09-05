# this is a path finding problem
# since it is a grid, it makes our life easy as well
# but we need to see the mathematical side of this. it's a permutation problem
# it is well explained in this article
# https://towardsdatascience.com/understanding-combinatorics-number-of-paths-on-a-grid-bddf08e28384

# here comes my explanation
# it is a 20x20 grid. For every path, the number of steps would be the same.
# meaning: for every path, you need to take 20 Rights and 20 Downs. 40 steps in total.
# All possible combinations = 40!
# (to get permutation of a string with RRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDD (20Rs and 20Ds)
# But, 40! also includes shuffling same letters together. (eg: R and R and R) means the same thing.
# so let's remove the repeated shuffling of the same letters by dividing. Since there are two letters with 20 each
# we divide by 20! for Rs and 20! for Ds
# our formula would be (number of steps * 2)! / ( (same direction D count!) * (same direction R count!) )
# we know that (number of steps) = Ds + Rs. In this example its 20+20 = 40. If the grid size is N, (number of steps) = 2N
# D count  = N, and R count = N
# final formula => (2N)!/(N!*N!)

import math


def get_symmetric_grid_paths(N):
    return math.factorial(2 * N) // (math.factorial(N) * math.factorial(N))


print(get_symmetric_grid_paths(20))





