import re

test_input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

debug_data = False
data = test_input.strip().split("\n")

if not debug_data:
    with open("13_input.txt", "r") as f:
        data = [line for line in f.readlines()]


button_pattern = re.compile(r".*X(.+\d+), Y(.+\d+)$")
prize_pattern = re.compile(r".*X=(.+\d+), Y=(.+\d+)$")


class Machine:
    def __init__(self):
        self.xa = 0
        self.ya = 0

        self.xb = 0
        self.yb = 0

        self.X = 0
        self.Y = 0

        self.cost_a = 3
        self.cost_b = 1

        self.button_limit = 100

    def __repr__(self):
        return f"Machine({self.xa=}, {self.ya=}, {self.xb=}, {self.yb=}, {self.X=}, {self.Y=})"

    def solve(self):

        A = (self.X * self.yb - self.xb * self.Y) / (self.xa * self.yb - self.xb * self.ya)
        B = (-self.X * self.ya + self.xa * self.Y) / (self.xa * self.yb - self.xb * self.ya)

        return A, B

    def get_token_prize(self):
        A, B = self.solve()

        if int(A) == A and int(B) == B:
            if self.button_limit:
                if A > self.button_limit and B > self.button_limit:
                    return False
            return int(A * self.cost_a) + int(B * self.cost_b)
        else:
            return False


machines = []
machine = Machine()

for i, line in enumerate(data):
    if i % 4 == 0:
        xa, ya = button_pattern.match(line).groups()
        machine.xa = int(xa)
        machine.ya = int(ya)
    elif i % 4 == 1:
        xb, yb = button_pattern.match(line).groups()
        machine.xb = int(xb)
        machine.yb = int(yb)
    elif i % 4 == 2:
        X, Y = prize_pattern.match(line).groups()
        machine.X = int(X)
        machine.Y = int(Y)
    else:
        machines.append(machine)
        machine = Machine()
machines.append(machine)

total_sum = 0
for machine in machines:
    if tokens := machine.get_token_prize():
        total_sum += tokens

print(f"First part: {total_sum}")

total_sum = 0
for machine in machines:
    machine.button_limit = False
    machine.X += 10000000000000
    machine.Y += 10000000000000
    if tokens := machine.get_token_prize():
        total_sum += tokens

print(f"Second part: {total_sum}")
