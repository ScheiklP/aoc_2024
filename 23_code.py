test_input = """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

with open("23_input.txt") as f:
    test_input = f.read()

connections = [(x.split("-")[0], x.split("-")[1]) for x in test_input.split("\n") if x]


computers = set()
for connection in connections:
    computers.add(connection[0])
    computers.add(connection[1])


groups = set()
for a, b in connections:
    ac = set([connection[0] if connection[1] == a else connection[1] for connection in connections if a in connection])
    bc = set([connection[0] if connection[1] == b else connection[1] for connection in connections if b in connection])
    cs = ac.intersection(bc)

    for c in cs:
        group = [a, b, c]
        groups.add(tuple(sorted(group)))

total = 0
for group in groups:
    starts_with_t = False
    for computer in group:
        if computer.startswith("t"):
            starts_with_t = True
            break
    if starts_with_t:
        total += 1
print(f"First part: {total}")


def down(possible_members, group):
    if not possible_members:
        return
    test_member = possible_members.pop()
    test_connections = list(set([connection[0] if connection[1] == test_member else connection[1] for connection in connections if test_member in connection]))

    sub_group = []
    for rest_member in possible_members:
        if rest_member in test_connections:
            sub_group.append(rest_member)

    group.append(test_member)

    down(sub_group, group)


groups = set()
for computer in computers:
    possible_members = list(set([connection[0] if connection[1] == computer else connection[1] for connection in connections if computer in connection]))
    group = [computer]
    down(possible_members, group)
    groups.add(tuple(sorted(group)))

max_len = 0
max_group = None
for group in groups:
    if len(group) > max_len:
        max_len = len(group)
        max_group = group

print(f"Second part:")
print(",".join(max_group))
