DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

input_file = "06_input.txt"
text = []
with open(input_file, "r") as f:
    for line in f.readlines():
        text.append([c for c in line.strip()])

test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# text = [[c for c in line] for line in test_input.strip().split("\n")]
max_i = len(text) - 1
max_j = len(text[0]) - 1

stop = False
guard_direction = 0
for i, line in enumerate(text):
    if stop:
        break
    for j, c in enumerate(line):
        if c == "^":
            cur_i, cur_j = i, j
            s_i, s_j = i, j
            stop = True

direction_history = [guard_direction]
visited_locations = [(cur_i, cur_j)]

hypothetical_loop_count = 0
hypothetical_loop_placements = []

while True:

    dir = DIRECTIONS[guard_direction]
    next_i, next_j = cur_i + dir[0], cur_j + dir[1]

    if not (0 <= next_i <= max_i and 0 <= next_j <= max_j):
        break

    next_character = text[next_i][next_j]
    if next_character == "#":
        guard_direction = (guard_direction + 1) % 4
    else:
        cur_i, cur_j = next_i, next_j
        visited_locations.append((cur_i, cur_j))
        direction_history.append(guard_direction)

print(f"First part: {len(set(visited_locations))}")

num_loops = 0
for o_i in range(max_i + 1):
    for o_j in range(max_j + 1):

        cur_i, cur_j = s_i, s_j
        guard_direction = 0

        locations_and_directions = set()
        locations_and_directions.add((cur_i, cur_j, guard_direction))

        while True:

            dir = DIRECTIONS[guard_direction]
            next_i, next_j = cur_i + dir[0], cur_j + dir[1]

            if not (0 <= next_i <= max_i and 0 <= next_j <= max_j):
                break

            next_character = text[next_i][next_j]
            if next_character == "#" or (next_i == o_i and next_j == o_j):
                guard_direction = (guard_direction + 1) % 4
            else:
                cur_i, cur_j = next_i, next_j

                if (cur_i, cur_j, guard_direction) in locations_and_directions:
                    num_loops += 1
                    break
                else:
                    locations_and_directions.add((cur_i, cur_j, guard_direction))

print(f"Second part: {num_loops}")
