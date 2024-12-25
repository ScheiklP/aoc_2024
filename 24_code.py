import graphviz

graph = graphviz.Digraph("adder")

operations = {
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
    "AND": lambda x, y: x & y,
}
colors = {
    "OR": "red",
    "XOR": "blue",
    "AND": "green",
}

file = "24_input.txt"

wire_values = {}
gates = {}
output_layer = []
input_x = []
input_y = []
with open(file, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if ":" in line:
            wire, value = line.split(":")
            wire_values[wire] = int(value)
            if wire.startswith("x"):
                input_x.append(wire)
            elif wire.startswith("y"):
                input_y.append(wire)
        elif "->" in line:
            gate, output_wire = line.split("->")
            wire_a, gate_type, wire_b = gate.split()
            output_wire = output_wire.strip()

            if output_wire.startswith("z"):
                output_layer.append(output_wire)

            gates[output_wire] = ((wire_a, wire_b), gate_type)

            graph.node(output_wire, output_wire)
            graph.node(wire_a, wire_a)
            graph.node(wire_b, wire_b)
            graph.edge(wire_a, output_wire, color=colors[gate_type])
            graph.edge(wire_b, output_wire, color=colors[gate_type])

input_x.sort()
input_y.sort()

graph.render("24_graph", format="pdf", cleanup=True, view=False)


def resolve(wire_o):

    if wire_o in wire_values:
        return wire_values[wire_o]

    (wire_a, wire_b), gate_type = gates[wire_o]

    if wire_a in wire_values:
        value_a = wire_values[wire_a]
    else:
        value_a = resolve(wire_a)

    if wire_b in wire_values:
        value_b = wire_values[wire_b]
    else:
        value_b = resolve(wire_b)

    return operations[gate_type](value_a, value_b)


output_layer.sort()
output_number = []
for output_wire in output_layer:
    output_number.append(resolve(output_wire))

output_number = "".join([str(i) for i in output_number[::-1]])
print(f"First part: {int(output_number, 2)}")


# Looked at the graph and found the following:
# Z is always output of XOR (except for the last one)
z_offender = []
# AND always outputs to OR (except for the first one)
and_offender = []
# OR never outputs to OR
# OR always outputs to AND, and an XOR that outpurs to Z
or_offender = []
# XOR never outputs to OR
xor_offender = []


for gate, value in gates.items():
    gate_type = value[1]
    if gate.startswith("z") and not gate == output_layer[-1]:
        if gate_type != "XOR":
            z_offender.append(gate)

    if gate_type == "AND":
        a = gate
        x, y = value[0]
        for gate, value in gates.items():
            if a in value[0]:
                if value[1] != "OR":
                    if x not in ("x00", "y00"):
                        and_offender.append(x)

    elif gate_type == "OR":
        a = gate
        for gate, value in gates.items():
            if a in value[0]:
                if value[1] == "OR":
                    or_offender.append(a)
                elif value[1] == "XOR":
                    if not gate.startswith("z"):
                        or_offender.append(gate)

    elif gate_type == "XOR":
        a = gate
        for gate, value in gates.items():
            if a in value[0]:
                if value[1] == "OR":
                    xor_offender.append(a)

output = sorted(list(set(and_offender + or_offender + xor_offender + z_offender)))
print("Second part:", ",".join(output))
