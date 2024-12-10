def print_nested_dict(d, indent=0):
    for key, value in d.items():
        print("  " * indent + str(key) + ":")
        if isinstance(value, dict):
            print_nested_dict(value, indent + 1)
        else:
            print("  " * (indent + 1) + str(value))


test_input = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

debug_data = False
topo_map = [[int(c) if c != "." else -1 for c in line] for line in test_input.strip().split("\n")]

if not debug_data:
    input_file = "./10_input.txt"

    with open(input_file, "r") as f:
        topo_map = [[int(c) if c != "." else -1 for c in line.strip()] for line in f.readlines()]

trail_heads = []

R = len(topo_map)
C = len(topo_map[0])

for r in range(R):
    for c in range(C):
        if topo_map[r][c] == 0:
            trail_heads.append((r, c, 0))

trails = {head: {} for head in trail_heads}


def hike(trail, peaks):
    for (r, c, l), sub_trail in trail.items():

        neighbor_locations = [
            (r, c + 1),
            (r - 1, c),
            (r, c - 1),
            (r + 1, c),
        ]

        for rn, cn in neighbor_locations:
            if 0 <= rn <= (R - 1) and 0 <= cn <= (C - 1):
                ln = topo_map[rn][cn]
                if ln == l + 1:
                    sub_trail[(rn, cn, ln)] = {}
                    if ln == 9:
                        peaks.append((rn, cn, ln))

        hike(sub_trail, peaks)


total_sum_1 = 0
total_sum_2 = 0
for trail_head in trail_heads:
    trail = {trail_head: {}}
    peaks = []
    hike(trail, peaks)
    if debug_data:
        print_nested_dict(trail)

    total_sum_1 += len(set(peaks))
    total_sum_2 += len(peaks)


print(f"First part: {total_sum_1}")
print(f"Second part: {total_sum_2}")
