test_input = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
debug_data = False
data = test_input.strip().split("\n")

towels = []
patterns = []

if not debug_data:
    with open("19_input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
for i, line in enumerate(data):
    if i == 0:
        towels = line.split(", ")
    else:
        if len(line):
            patterns.append(line)


num_possible_patterns = 0
for pat_num, pattern in enumerate(patterns):

    to_match = set()
    to_match.add(pattern)
    done = False
    num_solutions = 0

    while len(to_match):
        for check in to_match:
            if check in towels:
                num_possible_patterns += 1
                done = True
                break

        if not done:
            check = to_match.pop()
            if check in towels:
                num_possible_patterns += 1
                done = True
            for i in range(len(check)):
                sub_pattern = check[:i]
                if sub_pattern in towels:
                    remainder = check[i:]
                    to_match.add(remainder)
        else:
            break

print(f"First part: {num_possible_patterns}")
