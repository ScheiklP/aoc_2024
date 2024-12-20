from functools import cache

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


@cache
def exact_recursive(sub_pattern):
    solutions = 0
    for i in range(len(sub_pattern)):
        if sub_pattern[:i] in towels:
            if sub_pattern[i:] in towels:
                solutions += 1
            solutions += exact_recursive(sub_pattern[i:])
    return solutions


possible_patterns = 0
total_sum = 0
for pat_num, pattern in enumerate(patterns):
    new_possible_patterns = exact_recursive(pattern)
    total_sum += new_possible_patterns
    possible_patterns += 1 if new_possible_patterns > 0 else 0

print(f"First part: {possible_patterns}")
print(f"Second part: {total_sum}")
