import heapq

test_maze = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
test_score = 7036

test_maze2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
test_score2 = 11048

move_cost = 1
turn_cost = 1000

dirs = {
    0: (-1, 0),  # "^"
    1: (0, 1),  # ">"
    2: (1, 0),  # "v"
    3: (0, -1),  # "<"
}


grids = []
grid = [[c for c in line] for line in test_maze.strip().split("\n")]
grids.append(grid)
grid = [[c for c in line] for line in test_maze2.strip().split("\n")]
grids.append(grid)
with open("16_input.txt") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]
grids.append(grid)


costs = []
for i, grid in enumerate(grids):
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == "S":
                start = (r, c)
            if char == "E":
                end = (r, c)

    start_dir = 1
    start_r, start_c = start
    end_r, end_c = end

    rows = len(grid)
    cols = len(grid[0])
    # parents = [[[[] for _ in range(len(dirs))] for _ in range(cols)] for _ in range(rows)]

    directed_cost_grid = [[[float("inf") for _ in range(len(dirs))] for _ in range(cols)] for _ in range(rows)]
    directed_cost_grid[start_r][start_c][start_dir] = 0

    priority_queue = [(0, (start_r, start_c, start_dir))]

    while priority_queue:
        current_cost, (r, c, d) = heapq.heappop(priority_queue)

        # disabled for part 2
        # if (r, c) == (end_r, end_c):
        #     break

        if current_cost > directed_cost_grid[r][c][d]:
            continue

        neighbors = [
            ((r, c, (d + 1) % 4), turn_cost),  # clockwise turn
            ((r, c, (d - 1) % 4), turn_cost),  # counter-clockwise turn
            ((r + dirs[d][0], c + dirs[d][1], d), move_cost),  # move forward
        ]

        for (r2, c2, d2), cost in neighbors:
            if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] != "#":
                if current_cost + cost < directed_cost_grid[r2][c2][d2]:
                    directed_cost_grid[r2][c2][d2] = current_cost + cost
                    heapq.heappush(priority_queue, (current_cost + cost, (r2, c2, d2)))
                    # parents[r2][c2][d2] == [(r, c, d)]

                # elif current_cost + cost == directed_cost_grid[r2][c2][d2]:
                # parents[r2][c2][d2].append((r, c, d))

    optimal_paths = []

    for optimal_path in optimal_paths:
        for r, c in optimal_path:
            grid[r][c] = "O"
        grid[start_r][start_c] = "S"
        grid[end_r][end_c] = "E"

    if i != 2:
        to_print = "\n".join("".join(line) for line in grid)
        print(to_print)

    costs.append(
        min(
            (
                directed_cost_grid[end_r][end_c][0],
                directed_cost_grid[end_r][end_c][1],
                directed_cost_grid[end_r][end_c][2],
                directed_cost_grid[end_r][end_c][3],
            )
        )
    )

assert costs[0] == test_score
assert costs[1] == test_score2
print(f"First part: {costs[2]}")
