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
debug_data = True
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


def exact_recursive(sub_pattern):
    # Correct but too slow

    if sub_pattern in towels:
        return True

    remainders = []
    for i in range(len(sub_pattern)):
        if sub_pattern[:i] in towels:
            remainders.append(sub_pattern[i:])

    if len(remainders) == 0:
        return False

    possible = False
    for remainder in remainders:
        possible |= exact_recursive(remainder)

    return possible


def guess_recursive(sub_pattern):
    # Fast enough but incorrect (too few olutions because of guess)

    if sub_pattern in towels:
        return True

    for i in range(len(sub_pattern) - 1):
        check = sub_pattern[: -i - 1]
        if check in towels:
            remainder = sub_pattern[-i - 1 :]
            return guess_recursive(remainder)

    return False


num_possible_patterns = 0
possible_patterns = []
solutions = []
for pat_num, pattern in enumerate(patterns):

    to_match = set()
    to_match.add(pattern)
    done = False
    num_solutions = 0

    while len(to_match):
        # for check in to_match:
        #     if check in towels:
        #         num_possible_patterns += 1
        #         possible_patterns.append(pattern)
        #         done = True
        #         break

        if not done:
            check = to_match.pop()
            if check in towels:
                # num_possible_patterns += 1
                num_solutions += 1
                # possible_patterns.append(pattern)
                # done = True
            for i in range(len(check)):
                sub_pattern = check[:i]
                if sub_pattern in towels:
                    remainder = check[i:]
                    to_match.add(remainder)
        else:
            break

    num_possible_patterns += 1 if num_solutions > 0 else 0

    solutions.append(num_solutions)

print(solutions)


print(f"First part: {num_possible_patterns}")
