test_input = \
"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

TEXT = []
line = []
for c in test_input:
    if c == "\n":
        TEXT.append(line)
        line = []
    else:
        line.append(c)

input_file = "./04_input.txt"
TEXT = []
with open(input_file, "r") as f:
    for line in f.readlines():
        TEXT.append([c for c in line if c != "\n"])

def valid_location(i: int, j: int) -> bool:
    min_i = 0
    min_j = 0
    max_i = len(TEXT) - 1
    max_j = len(TEXT[0]) - 1

    i_valid = min_i <= i <= max_i
    j_valid = min_j <= j <= max_j

    return i_valid and j_valid

def look_for_mas(i, j):
    search_directions = []
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == b == 0:
                continue
            search_directions.append([
                [i+a, j+b, "M"], # M
                [i+a*2, j+b*2, "A"], # A
                [i+a*3, j+b*3, "S"], # S

            ])

    xmas_counter = 0
    for search_direction in search_directions:
        not_xmas = False
        for location in search_direction:
            if valid_location(location[0], location[1]):
                char = TEXT[location[0]][location[1]]
                if char != location[2]:
                    not_xmas = True
            else:
                not_xmas = True
        if not not_xmas:
            xmas_counter += 1

    return xmas_counter

possible_start_locations = []
for i, line in enumerate(TEXT):
    for j, char in enumerate(line):
        if char == "X":
            possible_start_locations.append([i, j])

total_hits = 0
for i, j in possible_start_locations:
    total_hits += look_for_mas(i, j)

print(f"First part: {total_hits}")


def look_for_xed_mas(i, j):

    diagonals = [
        [
            [i - 1, j - 1],
            [i + 1, j + 1],
        ],
        [
            [i - 1, j + 1],
            [i + 1, j - 1],
        ],
    ]

    invalid = False
    for diagonal in diagonals:
        chars = []
        for location in diagonal:
            if valid_location(location[0], location[1]):
                chars.append(TEXT[location[0]][location[1]])
        if set(chars) != {"M", "S"}:
            invalid = True

    if invalid:
        return 0
    else:
        return 1

possible_start_locations = []
for i, line in enumerate(TEXT):
    for j, char in enumerate(line):
        if char == "A":
            possible_start_locations.append([i, j])

total_hits = 0
for i, j in possible_start_locations:
    total_hits += look_for_xed_mas(i, j)

print(f"Second part: {total_hits}")
