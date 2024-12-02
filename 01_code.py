from collections import defaultdict

input_file = "01_input.txt"

first_list = []
second_list = []

with open(input_file, "r") as f:
    for line in f:
        first, second = line.split()
        first_list.append(int(first))
        second_list.append(int(second))

first_list.sort()
second_list.sort()

total_distance = 0
for first, second in zip(first_list, second_list):
    distance = abs(first - second)
    total_distance += distance

print(f"First part: {total_distance}")

count_dict = defaultdict(int)
for second in second_list:
    count_dict[second] += 1

total_score = 0
for first in first_list:
    total_score += count_dict[first] * first

print(f"Second part: {total_score}")
