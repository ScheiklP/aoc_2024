from collections import defaultdict
from functools import reduce

data = "0 1 10 99 999"
debug_data = False

if not debug_data:
    with open("./11_input.txt", "r") as f:
        data = f.readline()

stones = {c: 1 for c in data.strip().split()}

for i in range(75):
    updated_stones = defaultdict(int)
    for stone, weight in stones.items():
        if stone == "0":
            updated_stones["1"] += weight
        elif (digits := len(stone)) % 2 == 0:

            first = stone[: digits // 2].lstrip("0")
            second = stone[digits // 2 :].lstrip("0")

            if len(first) == 0:
                first = "0"

            if len(second) == 0:
                second = "0"

            updated_stones[first] += weight
            updated_stones[second] += weight

        else:
            updated_stones[str(int(stone) * 2024)] += weight

    if i == 24:
        print(f"First part: {reduce(lambda x, y: x + y, updated_stones.values())}")
    stones = updated_stones

print(f"Second part: {reduce(lambda x, y: x + y, stones.values())}")