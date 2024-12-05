input_file = "05_input.txt"
test_input_file = "05_test_input.txt"
# input_file = test_input_file

def update_is_valid(update, rules):
    valid_update = True
    for j, number in enumerate(update):
        left_of_number = update[:j]
        right_of_number = update[j+1:]

        left_rules = [rule[0] for rule in rules if number == rule[1]]
        right_rules = [rule[1] for rule in rules if number == rule[0]]

        left_violation = any([left_number in right_rules for left_number in left_of_number])
        right_violation = any([right_number in left_rules for right_number in right_of_number])

        violation = left_violation or right_violation

        if violation:
            valid_update = False

    return valid_update

rules = []
updates = []
with open(input_file, "r") as f:
    for line in f.readlines():
        if "|" in line:
            rules.append([int(number) for number in line.split("|") if number != "\n"])
        elif len(line.strip()) == 0:
            continue
        else:
            updates.append([int(number) for number in line.split(",") if number != "\n"])

invalid_updates = []
middle_number_of_valid_updates = []
for i, update in enumerate(updates):

    if update_is_valid(update, rules):
        assert len(update) % 2 == 1
        k = int(len(update) // 2)
        middle_number = update[k]
        middle_number_of_valid_updates.append(middle_number)
    else:
        invalid_updates.append(update)

print(f"First part: {sum(middle_number_of_valid_updates)}")


corrected_updates = []
for i, invalid_update in enumerate(invalid_updates):
    update = []
    while len(invalid_update):
        test_number = invalid_update.pop()
        for j in range(len(update)+1):
            tmp_update = update.copy()
            tmp_update.insert(j, test_number)
            if update_is_valid(tmp_update, rules):
                update = tmp_update
                break
    corrected_updates.append(update)

total_sum = 0
for update in corrected_updates:
    assert len(update) % 2 == 1
    k = int(len(update) // 2)
    middle_number = update[k]
    total_sum += middle_number

print(f"Second part: {total_sum}")


