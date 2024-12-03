import re
input_file = "03_input.txt"
test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
long_string = ""
with open(input_file, "r") as f:
    for line in f.readlines():
        long_string += line

pattern = re.compile(r"(don't\(\))|(do\(\))|mul\((\d{1,3}),(\d{1,3})\)" )
total_sum_1 = 0
total_sum_2 = 0
result = pattern.findall(long_string)
enabled = True
for matches in result:
    disable_flag = matches[0]
    enable_flag = matches[1]
    a = matches[2]
    b = matches[3]

    if len(a) and len(b):
        assert len(disable_flag) == 0
        assert len(enable_flag) == 0
        prod = int(a) * int(b)
        total_sum_1 += prod
        if enabled:
            total_sum_2 += prod

    if len(disable_flag):
        assert len(a) == 0
        assert len(b) == 0
        assert len(enable_flag) == 0
        enabled = False

    if len(enable_flag):
        assert len(a) == 0
        assert len(b) == 0
        assert len(disable_flag) == 0
        enabled = True


print(f"First part: {total_sum_1}")
print(f"Second part: {total_sum_2}")
