test_input = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

locks = []
keys = []


lines = test_input.strip().split("\n")
with open("25_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


locks = []

block_height = 8
for i in range(0, len(lines), block_height):
    if lines[i] == "#" * len(lines[i]):
        heights = [0] * len(lines[i])
        for line in lines[i + 1 : i + 7]:
            for j, c in enumerate(line):
                if c == "#":
                    heights[j] += 1
        locks.append(heights)
    elif lines[i] == "." * len(lines[i]):
        heights = [5] * len(lines[i])
        for line in lines[i + 1 : i + 7]:
            for j, c in enumerate(line):
                if c == ".":
                    heights[j] -= 1
        keys.append(heights)

pairs = 0
for lock in locks:
    for key in keys:
        fit = True
        for a, b in zip(lock, key):
            if a + b > 5:
                fit = False
        if fit:
            pairs += 1
print(f"First part: {pairs}")
