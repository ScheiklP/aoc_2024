from functools import cache

numpad = (
    (7, 8, 9),
    (4, 5, 6),
    (1, 2, 3),
    ("X", 0, "A"),
)

keypad = (
    ("X", "^", "A"),
    ("<", "v", ">"),
)

numpad_loc = {
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    0: (3, 1),
    "A": (3, 2),
}

keypad_loc = {
    "^": (0, 1),
    "v": (1, 1),
    "<": (1, 0),
    ">": (1, 2),
    "A": (0, 2),
}

keypad_moves = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


codes = (
    (0, 2, 9, "A"),
    (9, 8, 0, "A"),
    (1, 7, 9, "A"),
    (4, 5, 6, "A"),
    (3, 7, 9, "A"),
)

codes = [
    [3, 4, 1, "A"],
    [0, 8, 3, "A"],
    [8, 0, 2, "A"],
    [9, 7, 3, "A"],
    [7, 8, 0, "A"],
]


@cache
def get_instructions(start, goal, controller):
    loc_lookup = numpad_loc if controller is numpad else keypad_loc

    rs, cs = loc_lookup[start]
    rg, cg = loc_lookup[goal]

    rd = rg - rs
    cd = cg - cs
    moves = []
    moves.extend("v" if rd > 0 else "^" for _ in range(abs(rd)))
    moves.extend(">" if cd > 0 else "<" for _ in range(abs(cd)))

    symmetrical = moves == moves[::-1]
    if symmetrical:
        all_moves = [tuple(moves)]
    else:
        all_moves = [tuple(moves), tuple(moves[::-1])]

    valid_moves = []

    for moves in all_moves:
        r = rs
        c = cs
        valid = True
        for move in moves:
            r += keypad_moves[move][0]
            c += keypad_moves[move][1]
            if controller[r][c] == "X":
                valid = False
                break
        if valid:
            valid_moves.append(moves + ("A",))

    return tuple(valid_moves)


@cache
def down(possible_sequences, current_depth, max_depth):

    if current_depth == max_depth:
        return len(possible_sequences[0])

    min_layer_moves = float("inf")
    for sequence in possible_sequences:
        num_moves = 0

        for j in range(len(sequence)):
            start = "A" if j == 0 else sequence[j - 1]
            goal = sequence[j]
            moves = get_instructions(start, goal, keypad)

            num_moves += down(moves, current_depth + 1, max_depth)

            if num_moves > min_layer_moves:
                break

        min_layer_moves = min(min_layer_moves, num_moves)

    return min_layer_moves


total_p1 = 0
total_p2 = 0
for code in codes:

    num_moves_p1 = 0
    num_moves_p2 = 0
    for i in range(len(code)):
        start = "A" if i == 0 else code[i - 1]
        goal = code[i]
        numpad_robot_moves = get_instructions(start, goal, numpad)

        num_moves_p1 += down(numpad_robot_moves, 0, 2)
        num_moves_p2 += down(numpad_robot_moves, 0, 25)

    print(num_moves_p1)
    code_complexity_p1 = num_moves_p1 * int("".join(map(str, code[:-1])))
    code_complexity_p2 = num_moves_p2 * int("".join(map(str, code[:-1])))
    total_p1 += code_complexity_p1
    total_p2 += code_complexity_p2


print(f"First part: {total_p1}")
print(f"Second part: {total_p2}")
