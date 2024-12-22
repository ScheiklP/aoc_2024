from collections import defaultdict


def evolve(secret_number):
    step1 = secret_number * 64
    secret_number = secret_number ^ step1
    secret_number = secret_number % 16777216

    step2 = secret_number // 32
    secret_number = secret_number ^ step2
    secret_number = secret_number % 16777216

    step3 = secret_number * 2048
    secret_number = secret_number ^ step3
    secret_number = secret_number % 16777216

    return secret_number


with open("22_input.txt") as f:
    buyers = [int(line) for line in f]

buyer_prices = []
buyer_diffs = []
buyer_sequences = defaultdict(int)

total = 0

for buyer in buyers:
    sequences = {}
    prices = [int(str(buyer)[-1])]
    diffs = []
    for _ in range(2000):
        buyer = evolve(buyer)
        prices.append(int(str(buyer)[-1]))
        diffs.append(prices[-1] - prices[-2])

    buyer_prices.append(prices)
    buyer_diffs.append(diffs)

    for i in range(len(diffs) - 3):
        diff_seq = tuple(diffs[i : i + 4])
        seq_price = prices[i + 4]
        if diff_seq not in sequences:
            sequences[diff_seq] = seq_price

    for k, v in sequences.items():
        buyer_sequences[k] += v

    total += buyer

print(f"First part: {total}")

max_val = 0
max_key = None
for k, v in buyer_sequences.items():
    if v > max_val:
        max_val = v
        max_key = k

print(f"Second part: {max_key} -> {max_val}")
