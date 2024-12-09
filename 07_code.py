input_file = "07_input.txt"

with open(input_file, "r") as file:
    data = file.read().splitlines()

test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
test_data = test_input.strip().splitlines()

total_sum = 0


def down(res, vals, operators):

    if not len(vals):
        return False


    route_a = route_b = route_plus  = third_route = False

    if len(vals) >= 2:
        third_route = down(res, vals[:-2] + [int(f"{vals[-2]}{vals[-1]}")], operators)
        if third_route:
            operators.append("||")
            return True

    val = vals[-1]

    if res % val:
        res -= val
        if res == 0:
            operators.append("+")
            return True
        else:
            route_plus = down(res, vals[:-1], operators)
            if route_plus:
                operators.append("+")
                return True
    else:
        res_a = res - val
        if res_a == 0:
            return True
        else:
            route_a = down(res_a, vals[:-1], operators)
            if route_a:
                operators.append("+")
                return True

        res_b = res / val

        if res_b == 1:
            operators.append("*")
            return True
        else:
            route_b = down(res_b, vals[:-1], operators)
            if route_b:
                operators.append("*")
                return True

    return route_a or route_b or route_plus or third_route


#for line in data:
for line in test_data:
    result = int(line.split(": ")[0].strip())
    org_result = result
    values = line.split(": ")[1].strip()
    values = [int(val) for val in values.split()]

    operators = []
    if down(result, values, operators):
        total_sum += org_result
    print(operators)



print(total_sum)
