# this takes around 1 minute, but it gives the answer

def get_right_angle_combinations(perimeter):
    combinations = 0
    for a in range(1, perimeter // 3):
        for b in range(1, perimeter - a):
            c = perimeter - a - b
            if a ** 2 + b ** 2 == c ** 2:
                combinations += 1
    return combinations


# iterate from 3 to 1000 to see which perimeter has the biggest combination count
max = 0
selectedPerimeter = 0
for i in range(3,1000):
    count = get_right_angle_combinations(i)
    if max < count:
        max = count
        selectedPerimeter = i

print(selectedPerimeter)
