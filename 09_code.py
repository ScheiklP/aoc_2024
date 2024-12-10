disk_map = "2333133121414131402"
debug_data = False
debug_1 = False
debug_2 = False

if not debug_data:
    input_file = "09_input.txt"
    disk_map = open(input_file).read().strip()


def decode_disk_map(disk_map):
    decoded = []
    id_counter = 0
    for i, num in enumerate(disk_map):
        if i % 2:
            for _ in range(int(num)):
                decoded.append(f".")
        else:
            for _ in range(int(num)):
                decoded.append(f"{id_counter}")
            id_counter += 1
    return decoded


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

    if debug_1:
        debug = ["." for _ in range(len(decoded))]
        debug[empty_id] = "^"
        debug[file_block_id] = "°"
        print("".join(decoded))
        print("".join(debug))

    decoded[empty_id] = decoded[file_block_id]
    decoded[file_block_id] = "."

if debug_1:
    print("".join(decoded))

checksum = 0
for i, c in enumerate(decoded):
    if c == ".":
        continue

    checksum += int(c) * i

print(f"First part: {checksum}")


decoded = decode_disk_map(disk_map)
empty_id = 0
disk_map_len = len(decoded)
file_block_id = disk_map_len - 1
done = False
while not done:
    # Find the first file block from the end
    while decoded[file_block_id] == ".":
        file_block_id -= 1

    # How long is the file block?
    file_len = 0
    while decoded[file_block_id - file_len] == decoded[file_block_id]:
        file_len += 1
        if file_block_id - file_len < 0:
            done = True
            # file_block_id = 0
            break

    empty_id = 0
    while True:

        # Find the first empty block
        while not decoded[empty_id] == ".":
            empty_id += 1

        if empty_id > file_block_id:
            break

        # How long is the empty block?
        empty_len = 0
        while decoded[empty_id + empty_len] == ".":
            empty_len += 1

        # If the empty block can fit the file block, move the file block to the empty block
        if empty_len >= file_len:
            decoded[empty_id : empty_id + file_len] = decoded[file_block_id - file_len + 1 : file_block_id + 1]
            decoded[file_block_id - file_len + 1 : file_block_id + 1] = ["." for _ in range(file_len)]
            break
        else:
            # If the empty block is too small, advance the index to the next empty block
            empty_id += empty_len

    file_block_id -= file_len

    if debug_2:
        debug = ["." for _ in range(len(decoded))]
        debug[empty_id] = "^"
        debug[file_block_id] = "°"
        print("".join(decoded))
        print("".join(debug))


if debug_data:
    print("".join(decoded))

checksum = 0
for i, c in enumerate(decoded):
    if c == ".":
        continue

    checksum += int(c) * i

print(f"Second part: {checksum}")
