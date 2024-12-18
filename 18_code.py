import heapq


blocks = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

debug_data = False

R = 7 if debug_data else 71
C = 7 if debug_data else 71

data = [(int(x), int(y)) for x, y in (line.split(",") for line in blocks.strip().split("\n"))]

if not debug_data:
    with open("18_input.txt", "r") as f:
        data = [(int(x), int(y)) for x, y in (line.strip().split(",") for line in f.readlines())]

grid = [["." for _ in range(C)] for _ in range(R)]

for i, (xd, yd) in enumerate(data):
    grid[yd][xd] = "#"
    cost = [[float("inf") for _ in range(C)] for _ in range(R)]

    xs, ys = 0, 0
    xg, yg = C - 1, R - 1

    # cost, x, y
    priority_queue = [(0, 0, 0)]

    while len(priority_queue):

        current_cost, x, y = heapq.heappop(priority_queue)

        if current_cost > cost[y][x]:
            continue

        neighbors = [
            (y - 1, x),
            (y, x + 1),
            (y + 1, x),
            (y, x - 1),
        ]

        for yn, xn in neighbors:
            if 0 <= yn < R and 0 <= xn < C and grid[yn][xn] != "#":
                if current_cost + 1 < cost[yn][xn]:
                    cost[yn][xn] = current_cost + 1
                    heapq.heappush(priority_queue, (current_cost + 1, xn, yn))

    if i == 1023:
        print(f"First part: {cost[yg][xg]}")

    if cost[yg][xg] == float("inf"):
        print(f"Second part: {xd},{yd}")
        break
