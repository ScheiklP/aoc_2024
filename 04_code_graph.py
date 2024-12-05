"""Funny but incorrect solution. I thought the words were also allowed to bend, so this code does a recursive
kind of a graph traversal."""

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

TARGET_WORD = ["X", "M", "A", "S"]

TEXT = []
line = []
for c in test_input:
    if c == "\n":
        TEXT.append(line)
        line = []
    else:
        line.append(c)

def valid_location(i: int, j: int) -> bool:
    min_i = 0
    min_j = 0
    max_i = len(TEXT) - 1
    max_j = len(TEXT[0]) - 1

    i_valid = min_i <= i <= max_i
    j_valid = min_j <= j <= max_j

    return i_valid and j_valid

def get_neighbors(i, j):

    locations = []
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == b == 0:
                continue
            locations.append([i+a, j+b])

    neighbor_chars = []
    neighbor_locations = []
    # print_text = []
    # for _ in range(len(TEXT)):
        # print_text.append(["."] * len(TEXT[0]))

    for location in locations:
        if valid_location(location[0], location[1]):
            # print_text[location[0]][location[1]] =  TEXT[location[0]][location[1]]
            neighbor_chars.append(TEXT[location[0]][location[1]])
            neighbor_locations.append(location)

    # print_text = "\n".join(["".join(line) for line in print_text])
    # print(print_text)

    return neighbor_chars, neighbor_locations

data = {}
word_counter = []
char_pos = 0
possible_start_locations = []
for i, line in enumerate(TEXT):
    for j, char in enumerate(line):
        if char == TARGET_WORD[char_pos]:
            possible_start_locations.append([i, j])
            data[(i, j, char_pos)] = {}

def traverse(data, word_counter):
    for location, sub_data in data.items():
        char_pos = location[2]
        if char_pos == len(TARGET_WORD) - 1:
            word_counter.append(True)
            continue
        neighbor_chars, neighbor_locations = get_neighbors(location[0], location[1])
        for neighbor_char, neighbor_location in zip(neighbor_chars, neighbor_locations):
            if neighbor_char == TARGET_WORD[char_pos + 1]:
                sub_data[(neighbor_location[0], neighbor_location[1], char_pos + 1)] = {}
        print(location)
        print(sub_data)
        print()
        traverse(sub_data, word_counter)



traverse(data, word_counter)
print(len(word_counter))



