from collections import deque

test_input = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

debug_data = True
data = test_input.split("\n")
if not debug_data:
    with open("15_input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

matrix = []
movements = []
for line in data:
    if "#" in line:
        matrix.append([c for c in line.strip()])
    elif len(line.strip()) == 0:
        pass

    else:
        movements.extend([c for c in line.strip()])

robot_pos = None
for i, line in enumerate(matrix):
    for j, c in enumerate(line):
        if c == "@":
            robot_pos = (i, j)
            break

r, c = robot_pos

dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}

for movement in movements:
    if debug_data:
        to_print = "\n".join(["".join(line) for line in matrix])
        print(to_print)

    rn = r + dirs[movement][0]
    cn = c + dirs[movement][1]
    char = matrix[rn][cn]

    if char == "#":
        continue
    elif char == ".":
        # put . at old robot pos
        matrix[r][c] = "."

        # put @ at new robot pos
        r = rn
        c = cn
        matrix[r][c] = "@"

    if char == "O":
        rx = rn + dirs[movement][0]
        cx = cn + dirs[movement][1]

        next = []
        next.append(matrix[rx][cx])

        move = False
        while len(next):
            char = next.pop()
            if char == "O":
                rx += dirs[movement][0]
                cx += dirs[movement][1]
                next.append(matrix[rx][cx])
            elif char == "#":
                next = []
                move = False
            else:
                # destination
                rd, cd = rx, cx
                move = True
                next = []

        if move:
            # put . at old robot pos
            matrix[r][c] = "."

            # put @ at new robot pos
            r = rn
            c = cn
            matrix[r][c] = "@"

            # put O at the pos where the Os are pushed to
            matrix[rd][cd] = "O"

cost = 0
for i, line in enumerate(matrix):
    for j, c in enumerate(line):
        if c == "O":
            cost += 100 * i + j

print(f"First part: {cost}")


expanded_matrix = []
for i, line in enumerate(matrix):
    expanded_line = []
    for j, c in enumerate(line):
        if c == "#":
            expanded_line.extend(["#", "#"])
        elif c == ".":
            expanded_line.extend([".", "."])
        elif c == "O":
            expanded_line.extend(["[", "]"])
        elif c == "@":
            expanded_line.extend(["@", "."])
    expanded_matrix.append(expanded_line)
matrix = expanded_matrix

robot_pos = None
for i, line in enumerate(matrix):
    for j, c in enumerate(line):
        if c == "@":
            robot_pos = (i, j)
            break
r, c = robot_pos
