import heapq
from collections import defaultdict


def dijkstra(grid, rs, cs, rg, cg):
    pq = []
    cost = [[float("inf") for _ in range(C)] for _ in range(R)]

    cost[rs][cs] = 0
    pq.append((0, rs, cs))
    while len(pq):
        cc, r, c = heapq.heappop(pq)

        if (r, c) == (rg, cg):
            continue

        if cc > cost[r][c]:
            continue

        neighbors = [
            (r + 1, c),
            (r - 1, c),
            (r, c + 1),
            (r, c - 1),
        ]

        for rn, cn in neighbors:
            if 0 <= rn < R and 0 <= cn < C and cost[rn][cn] > cc + 1 and grid[rn][cn] == ".":
                cost[rn][cn] = cc + 1
                heapq.heappush(pq, (cc + 1, rn, cn))

    return cost


test_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

debud_data = False
data = test_input.strip().splitlines()

if not debud_data:
    with open("20_input.txt") as f:
        data = f.read().strip().splitlines()

grid = []
cheat_starts = []
for r, line in enumerate(data):
    new_line = []
    for c, char in enumerate(line):
        n_char = char if char in (".", "#") else "."
        if char == "S":
            rs, cs = r, c
        elif char == "E":
            rg, cg = r, c
        elif char != "#":
            cheat_starts.append((r, c))

        new_line.append(n_char)
    grid.append(new_line)


R, C = len(grid), len(grid[0])

cost_grid = dijkstra(grid, rs, cs, rg, cg)

r, c = rs, cs
savings = defaultdict(int)
path = []
while not (r, c) == (rg, cg):
    neighbors = [
        (r + 1, c),
        (r - 1, c),
        (r, c + 1),
        (r, c - 1),
    ]

    for rn, cn in neighbors:
        if grid[rn][cn] == "." and cost_grid[rn][cn] == cost_grid[r][c] + 1:
            r, c = rn, cn
            path.append((r, c))
            break


def get_manhatten_neighbors(r, c, dist):
    neighbors = []
    for i in range(-dist, dist + 1):
        for j in range(-dist, dist + 1):
            if abs(i) + abs(j) <= dist:
                neighbors.append((r + i, c + j))
    return neighbors


major_save = 0
for r, c in reversed(path):
    neighbors = get_manhatten_neighbors(r, c, 2)
    for rn, cn in neighbors:
        if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] == ".":
            saving = cost_grid[r][c] - cost_grid[rn][cn] - (abs(r - rn) + abs(c - cn))
            if saving > (0 if debud_data else 99):
                major_save += 1

print(f"First part: {major_save}")

major_save = 0
for r, c in reversed(path):
    neighbors = get_manhatten_neighbors(r, c, 20)

    for rn, cn in neighbors:
        if 0 <= rn < R and 0 <= cn < C and grid[rn][cn] == ".":
            saving = cost_grid[r][c] - cost_grid[rn][cn] - (abs(r - rn) + abs(c - cn))
            if saving > 0:
                savings[saving] += 1
            if saving > (49 if debud_data else 99):
                major_save += 1

print(f"Second part: {major_save}")
