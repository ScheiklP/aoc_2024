import re
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

test_input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
data = test_input.strip().split("\n")

with open("14_input.txt", "r") as f:
    data = [line for line in f.readlines()]

X = 101
Y = 103
seconds = 100

pattern = re.compile(r"p=(\d+),(\d+) v=(.*\d+),(.*\d+)")
robots = []
for line in data:
    x, y, vx, vy = pattern.match(line).groups()
    robots.append((int(x), int(y), int(vx), int(vy)))

quad_cound = [0] * 4
for x, y, vx, vy in robots:
    x += seconds * vx
    x = x % X

    y += seconds * vy
    y = y % Y

    if x == X // 2 or y == Y // 2:
        continue

    if x < X / 2 and y < Y / 2:
        quad_cound[0] += 1

    elif x < X / 2 and y > Y / 2:
        quad_cound[1] += 1

    elif x > X / 2 and y > Y / 2:
        quad_cound[2] += 1

    elif x > X / 2 and y < Y / 2:
        quad_cound[3] += 1


print(quad_cound[0] * quad_cound[1] * quad_cound[2] * quad_cound[3])


def calculate_entropy(grid):
    flattened = np.array(grid).flatten()
    # Count occurrences of each unique value
    counts = Counter(flattened)
    total_cells = flattened.size
    # Calculate probabilities
    probabilities = np.array([count / total_cells for count in counts.values()])
    # Calculate entropy
    entropy = -np.sum(probabilities * np.log2(probabilities))  # Use np.log2 for base-2 entropy
    return entropy


def calculate_fisher_information(grid):
    grid = np.array(grid, dtype=float)
    # Compute gradients in both directions
    gradient_i = np.gradient(grid, axis=0)  # Partial derivative w.r.t. rows
    gradient_j = np.gradient(grid, axis=1)  # Partial derivative w.r.t. columns
    # Fisher information is the sum of squared gradients
    fisher_info = np.sum(gradient_i**2 + gradient_j**2)
    return fisher_info


i = 0
fisher = []
shannon = []
while True:
    grid = [[0] * X for _ in range(Y)]
    for x, y, vx, vy in robots:
        x += i * vx
        x = x % X

        y += i * vy
        y = y % Y

        grid[y][x] += 1

    fisher.append(calculate_fisher_information(grid))
    shannon.append(calculate_entropy(grid))

    i += 1
    if i > 10_000:
        break


# 4x4 plot
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(fisher)
axs[0, 0].set_title("Fisher Information")
axs[0, 1].plot(shannon)
axs[0, 1].set_title("Shannon Entropy")
min_fisher = np.argmin(fisher)

grid = [[0] * X for _ in range(Y)]
for x, y, vx, vy in robots:
    x += min_fisher * vx
    x = x % X

    y += min_fisher * vy
    y = y % Y

    grid[y][x] += 1
axs[1, 0].imshow(grid, cmap="hot")
axs[1, 0].set_title("Fisher Information Minimum")


min_shannon = np.argmin(shannon)
grid = [[0] * X for _ in range(Y)]
for x, y, vx, vy in robots:
    x += min_shannon * vx
    x = x % X

    y += min_shannon * vy
    y = y % Y

    grid[y][x] += 1
axs[1, 1].imshow(grid, cmap="hot")
axs[1, 1].set_title("Shannon Entropy Minimum")

plt.show()

print(f"Minimum Fisher Information: {min_fisher}")
print(f"Minimum Shannon Entropy: {min_shannon}")
