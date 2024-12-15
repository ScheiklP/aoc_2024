import re

test_input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
data = test_input.strip().split("\n")

with open("14_input.txt", "r") as f:
    data = [line for line in f.readlines()]

X = 101
Y = 103
seconds = 100

pattern = re.compile(r"p=(\d+),(\d+) v=(.*\d+),(.*\d+)")
robots = []
for line in data:
    x, y, vx, vy = pattern.match(line).groups()
    robots.append((int(x), int(y), int(vx), int(vy)))

quad_cound = [0] * 4
for x, y, vx, vy in robots:
    x += seconds * vx
    x = x % X

    y += seconds * vy
    y = y % Y

    if x == X // 2 or y == Y // 2:
        continue

    if x < X / 2 and y < Y / 2:
        quad_cound[0] += 1

    elif x < X / 2 and y > Y / 2:
        quad_cound[1] += 1

    elif x > X / 2 and y > Y / 2:
        quad_cound[2] += 1

    elif x > X / 2 and y < Y / 2:
        quad_cound[3] += 1


print(quad_cound[0] * quad_cound[1] * quad_cound[2] * quad_cound[3])
