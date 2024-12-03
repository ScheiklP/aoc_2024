input_file = "02_input.txt"
test_input = "02_test_input.txt"

def same_sign(differences):
    positive = [x > 0 for x in differences]
    negative = [x < 0 for x in differences]
    return all(positive) or all(negative)

def in_range(differences):
    return all([abs(x) <=3 for x in differences])

with open(input_file, "r") as f:
    lines = [[int(num) for num in line.split()] for line in f.readlines()]

safe_lines = 0
for line in lines:
    differences = [line[i] - line[i-1] for i in range(1, len(line))]
    safe = False
    if same_sign(differences) and in_range(differences):
        safe = True
    if safe:
        safe_lines += 1

print(f"First part: {safe_lines}")

safe_lines = 0
for line in lines:
    differences = [line[i] - line[i-1] for i in range(1, len(line))]
    if same_sign(differences) and in_range(differences):
        safe_lines += 1
    else:
        for i in range(len(line)):
            subline = line[:i] + line[i+1:]
            differences = [subline[i] - subline[i-1] for i in range(1, len(subline))]
            if same_sign(differences) and in_range(differences):
                safe_lines += 1
                break

print(f"Second part: {safe_lines}")
