from matplotlib import pyplot as plt

data = "0 1 10 99 999"
debug_data = False

if not debug_data:
    with open("./11_input.txt", "r") as f:
        data = f.readline()


stones = [c for c in data.strip().split()]

lens = []
for i in range(25):
    updated_stones = []
    for stone in stones:
        if stone == "0":
            updated_stones.append("1")
        elif (digits := len(stone)) % 2 == 0:

            first = stone[: digits // 2].lstrip("0")
            second = stone[digits // 2 :].lstrip("0")

            if len(first) == 0:
                first = "0"

            if len(second) == 0:
                second = "0"

            updated_stones.append(first)
            updated_stones.append(second)

        else:
            updated_stones.append(str(int(stone) * 2024))

    stones = updated_stones
    lens.append(len(stones))

print(f"First part: {len(stones)}")

plt.plot(range(25), lens)
plt.show()

stones = [c for c in data.strip().split()]
# total_sum = 0
# for parent_stone in stones:
#     check_stones = [parent_stone]
#     for i in range(75):
#         updated_stones = []
#         for stone in check_stones:
#             if stone == "0":
#                 updated_stones.append("1")
#             elif (digits := len(stone)) % 2 == 0:

#                 first = stone[: digits // 2].lstrip("0")
#                 second = stone[digits // 2 :].lstrip("0")

#                 if len(first) == 0:
#                     first = "0"

#                 if len(second) == 0:
#                     second = "0"

#                 updated_stones.append(first)
#                 updated_stones.append(second)

#             else:
#                 updated_stones.append(str(int(stone) * 2024))

#         check_stones = updated_stones

#     total_sum += len(check_stones)

# print(f"Second part: {total_sum}")


# def down(num, i, depth=74):
#     print(num, i, depth)
#     if i == depth:
#         return

#     if stone == "0":
#         down("1", i + 1, depth)
#     elif (digits := len(num)) % 2 == 0:

#         first = num[: digits // 2].lstrip("0")
#         second = num[digits // 2 :].lstrip("0")

#         if len(first) == 0:
#             first = "0"

#         if len(second) == 0:
#             second = "0"

#         down(first, i + 1, depth)
#         down(second, i + 1, depth)
#     else:
#         down(str(int(num) * 2024), i + 1, depth)


# for stone in stones:
#     down(stone, 0, 74)
