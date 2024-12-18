from z3 import *

register_map = {
    "A": 4,
    "B": 5,
    "C": 6,
}


def ADV(operand):
    # Division of register A by 2^combo operand
    memory[register_map["A"]] = int(memory[register_map["A"]] / 2 ** memory[operand])
    instruction_pointer[0] += 2


def BDV(operand):
    # Division of register A by 2^combo operand
    memory[register_map["B"]] = int(memory[register_map["A"]] / 2 ** memory[operand])
    instruction_pointer[0] += 2


def CDV(operand):
    # Division of register A by 2^combo operand
    memory[register_map["C"]] = int(memory[register_map["A"]] / 2 ** memory[operand])
    instruction_pointer[0] += 2


def BXL(operand):
    # Bitwise XOR of register B with operand
    memory[register_map["B"]] = memory[register_map["B"]] ^ operand
    instruction_pointer[0] += 2


def BST(operand):
    # Cut down to 3 bits
    memory[register_map["B"]] = memory[operand] % 8
    instruction_pointer[0] += 2


def JNZ(operand):
    if memory[register_map["A"]] != 0:
        instruction_pointer[0] = operand
    else:
        instruction_pointer[0] += 2


def BXC(operand):
    memory[register_map["B"]] = memory[register_map["B"]] ^ memory[register_map["C"]]
    instruction_pointer[0] += 2


def OUT(operand):
    outputs.append(memory[operand] % 8)
    instruction_pointer[0] += 2


instructions = {
    0: ADV,
    1: BXL,
    2: BST,
    3: JNZ,
    4: BXC,
    5: OUT,
    6: BDV,
    7: CDV,
}


# Instruction, Operand
program = [2, 4, 1, 1, 7, 5, 4, 6, 0, 3, 1, 4, 5, 5, 3, 0]
instruction_pointer = [0]
outputs = []
memory = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 28066687,  # register A
    5: 0,  # register B
    6: 0,  # register C
    7: None,
}

while instruction_pointer[0] < len(program):
    instruction = program[instruction_pointer[0]]
    operand = program[instruction_pointer[0] + 1]
    instructions[instruction](operand)


print("First part:", ",".join(map(str, outputs)))

# Write down the executed instructions, and find a loop.
# These instruction loops are the basis for the Z3 solver


def find_register_a(output_sequence, max_bits=64):
    opt = Optimize()
    s = BitVec("s", max_bits)

    # Start with the unknown value of register A
    a, b, c = s, 0, 0

    # Execute the program loop
    for x in output_sequence:
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ c
        a = a / 8
        b = b ^ 4

        # and add a constraint, that the output of the loop
        # equals the current value of the program
        opt.add(b % 8 == x)

    opt.minimize(s)
    assert str(opt.check()) == "sat"
    print(f"Second part: {opt.model().eval(s)}")


find_register_a(program)
