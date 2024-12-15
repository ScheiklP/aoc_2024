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

debug_data = False
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
dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}
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

for movement in movements:
    if debug_data:
        to_print = "\n".join(["".join(line) for line in matrix])
        print(to_print)

    rn = r + dirs[movement][0]
    cn = c + dirs[movement][1]
    charn = matrix[rn][cn]

    move_data = [((r, c, "@"), (rn, cn, charn))]
    todo = deque()
    todo.append(((r, c, "@"), (rn, cn, charn)))

    move = True
    while len(todo) and move:
        to_check = todo.popleft()
        char_to_check = to_check[1][2]
        r_to_check, c_to_check = to_check[1][:2]

        if char_to_check == ".":
            continue
        elif char_to_check == "#":
            move = False

        elif char_to_check in ("[", "]"):
            rx = r_to_check + dirs[movement][0]
            cx = c_to_check + dirs[movement][1]
            char_x = matrix[rx][cx]
            new = ((r_to_check, c_to_check, char_to_check), (rx, cx, char_x))
            if new not in move_data:
                todo.append(new)
                move_data.append(new)

            if char_to_check == "[":
                rx = r_to_check + dirs[movement][0]
                cx = c_to_check + dirs[movement][1] + 1
                char_x = matrix[rx][cx]
                new = ((r_to_check, c_to_check+1, "]"), (rx, cx, char_x))
                if new not in move_data:
                    todo.append(new)
                    move_data.append(new)
            elif char_to_check == "]":
                rx = r_to_check + dirs[movement][0]
                cx = c_to_check + dirs[movement][1] - 1
                char_x = matrix[rx][cx]
                new = ((r_to_check, c_to_check-1, "["), (rx, cx, char_x))
                if new not in move_data:
                    todo.append(new)
                    move_data.append(new)

    if move:
        for a, b in move_data[::-1]:
            ca = matrix[a[0]][a[1]]
            cb = matrix[b[0]][b[1]]
            matrix[b[0]][b[1]] = ca
            matrix[a[0]][a[1]] = cb
        r = rn
        c = cn

cost = 0
for i, line in enumerate(matrix):
    for j, c in enumerate(line):
        if c == "[":
            cost += 100 * i + j

print(f"Second part: {cost}")
