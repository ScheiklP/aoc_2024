test_input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
data = test_input.strip()
test_data = True
matrix = [[c for c in line.strip()] for line in data.split("\n")]

if not test_data:
    matrix = []
    with open("12_input.txt", "r") as f:
        matrix = [[c for c in line.strip()] for line in f.readlines()]


def grow(region, r, c, p):
    neighbor_locations = (
        (r, c + 1),
        (r - 1, c),
        (r, c - 1),
        (r + 1, c),
    )

    for rn, cn in neighbor_locations:
        if 0 <= rn < R and 0 <= cn < C:
            pn = matrix[rn][cn]
            if pn == p:
                if (rn, cn, pn) not in new_region:
                    region.add((rn, cn, pn))
                    grow(region, rn, cn, pn)


R = len(matrix)
C = len(matrix[0])
print(R)
print(C)

regions = []
checked = []
for r in range(R):
    for c in range(C):
        p = matrix[r][c]
        if (r, c, p) in checked:
            continue

        new_region = set()
        new_region.add((r, c, p))

        grow(new_region, r, c, p)

        checked.extend(new_region)
        regions.append(new_region)

fence_price = 0
for region in regions:
    fence_len = 0
    for r, c, p in region:
        neighbor_locations = (
            (r, c + 1),
            (r - 1, c),
            (r, c - 1),
            (r + 1, c),
        )

        num_neighbors = 0
        for rn, cn in neighbor_locations:
            if (rn, cn, p) in region:
                num_neighbors += 1

        fence_len += 4 - num_neighbors

    fence_price += len(region) * fence_len


print(f"First part: {fence_price}")


def get_num_neighbors(r, c, p, region):
    neighbor_locations = (
        (r + 1, c),
        (r, c + 1),
        (r - 1, c),
        (r, c - 1),
    )

    dirs = []
    num_neighbors = 0
    for i, (rn, cn) in enumerate(neighbor_locations):
        if (rn, cn, p) in region:
            num_neighbors += 1
            dirs.append(i)

    return dirs


dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

for region in regions:
    for r, c, p in region:

        neighbor_dirs = get_num_neighbors(r, c, p, region)
        rd, cd = dirs[neighbor_dirs[0]]

        neighbor_dirs = get_num_neighbors(r + rd, c + cd, p, region)

        # len(dirs)==3 -> the one that is not in line adds 3 fence pieces. walk one way in line
        # len(dirs)==4 -> fully surrounded. does not add. walk out until you hit one smaller that 4
        # len(dirs)==2 -> either a corner (even and uneven dir) or a line (both even / uneven)
        # len(dirs)==1 -> edge. either add 1 or 3....


        if (rd, cd) in neighbor_dirs:
            print("A")

    exit()
