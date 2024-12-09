from copy import deepcopy

disk_map = "2333133121414131402"


def decode_disk_map(disk_map):
    decoded = ""
    id_counter = 0
    for i, num in enumerate(disk_map):
        if i % 2:
            decoded += int(num) * "."
        else:
            decoded += f"{id_counter}" * int(num)
            id_counter += 1

    return [c for c in decoded]


decoded = decode_disk_map(disk_map)

empty_id = 0
file_block_id = len(decoded) - 1
while True:
    while not decoded[empty_id] == ".":
        empty_id += 1

    while decoded[file_block_id] == ".":
        file_block_id -= 1

    if empty_id > file_block_id:
        break

    debug = ["." for _ in range(len(decoded))]
    debug[empty_id] = "^"
    debug[file_block_id] = "°"

    print("".join(decoded))
    print("".join(debug))

    decoded[empty_id] = decoded[file_block_id]
    decoded[file_block_id] = "."

print("".join(decoded))

checksum = 0
for i, c in enumerate(decoded):
    if c == ".":
        continue

    checksum += int(c) * i

print(checksum)
