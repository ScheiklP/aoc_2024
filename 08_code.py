from collections import defaultdict

input_file = "08_input.txt"


with open(input_file, "r") as f:
    matrix = [[c for c in line.strip()] for line in f.readlines() if len(line)]

test_input = """............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............"""

# matrix = [[c for c in line.strip()] for line in test_input.splitlines() if len(line)]

R = len(matrix)
C = len(matrix[0])

antenna_locations = defaultdict(list)

for r in range(R):
    for c in range(C):
        char = matrix[r][c]
        if char != ".":
            antenna_locations[char].append((r, c))


antinodes = set()
antinodes_part_2 = set()
for freq, locs in antenna_locations.items():
    for loc in locs:
        for other_loc in locs:
            if loc != other_loc:
                dr = other_loc[0] - loc[0]
                dc = other_loc[1] - loc[1]
                anti_r = other_loc[0] + dr
                anti_c = other_loc[1] + dc

                antinodes_part_2.add(loc)
                antinodes_part_2.add(other_loc)

                if 0 <= anti_r < R and 0 <= anti_c < C:
                    antinodes.add((anti_r, anti_c))

                while 0 <= anti_r < R and 0 <= anti_c < C:
                    antinodes_part_2.add((anti_r, anti_c))
                    anti_r += dr
                    anti_c += dc


print(len(antinodes))
print(len(antinodes_part_2))

for r, c in antinodes:
    matrix[r][c] = "#"

# print("\n".join(["".join(line) for line in matrix]))
