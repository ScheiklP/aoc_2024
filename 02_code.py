input_file = "02_input.txt"
test_input = "02_test_input.txt"

input_file = test_input
def same_sign(differences):
    positive = [x > 0 for x in differences]
    negative = [x < 0 for x in differences]
    return all(positive) or all(negative)

def in_range(differences):
    return all([abs(x) <=3 for x in differences])

def sign(x):
    return (x > 0) - (x < 0)


with open(input_file, "r") as f:
    lines = [[int(num) for num in line.split()] for line in f.readlines()]

indices = []
safe_lines = 0
for j, line in enumerate(lines):
    differences = [line[i] - line[i-1] for i in range(1, len(line))]
    safe = False
    if same_sign(differences) and in_range(differences):
        safe = True

    if safe:
        safe_lines += 1
    else:
        indices.append(j)

print(f"First part: {safe_lines}")

safe_lines = 0
for j, line in enumerate(lines):
    differences = []
    signs = []
    changes_not_in_range = []
    for i in range(1, len(line)):
        difference = line[i] - line[i-1]
        differences.append(difference)
        signs.append(sign(difference))
        changes_not_in_range.append(abs(difference)>3)
    sign_change = [False] + [(signs[i-1] != signs[i]) or signs[i] == 0 for i in range(1, len(signs))]

    unsafe = True
    if sum(sign_change) > 1 or sum(changes_not_in_range) > 1:
        unsafe = True
        continue

    if sum(sign_change) == 0 and sum(changes_not_in_range) == 0:
        unsafe = False
        safe_lines += 1
        continue

    if sum(sign_change) == 1:
        sign_offender = sign_change.index(True)
        new_line = [num for i, num in enumerate(line) if i != sign_offender]
        new_differences = [new_line[i] - new_line[i-1] for i in range(1, len(new_line))]
        print("Sign")
        print(f"old_line={line}")
        print(f"{new_line=}")
        print(f"{new_differences=}")
        if same_sign(new_differences) and in_range(new_differences):
            print("YO!")
            safe_lines += 1
            continue
        print()

    if sum(changes_not_in_range) == 1:
        print("Range")
        range_offender = changes_not_in_range.index(True)
        new_line = [num for i, num in enumerate(line) if i != range_offender]
        new_differences = [new_line[i] - new_line[i-1] for i in range(1, len(new_line))]
        print(f"old_line={line}")
        print(f"{new_line=}")
        print(f"{new_differences=}")
        if same_sign(new_differences) and in_range(new_differences):
            print("YO!")
            safe_lines += 1
        print()

print(f"Second part: {safe_lines}")
