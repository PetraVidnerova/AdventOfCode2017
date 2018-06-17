registers = {}
multiples = 0 

def value(y):
    if y in 'abcdefgh':
        return registers.get(y, 0)
    else:
        return int(y)

def set(x, y):
    print(" SET ")
    registers[x] = value(y)
    return 1

def sub(x, y):
    print(" SUB  ")
    registers[x] = registers.get(x, 0) - value(y)
    return 1

def mul(x, y):
    print(" MUL ")
    global multiples
    registers[x] = registers.get(x, 0) * value(y)
    multiples += 1
    return 1


def jnz(x, y):
    print(" JNZ ")
    if value(x) != 0:
        return value(y)
    else:
        return 1

instructions = { "set": set,
                 "sub": sub,
                 "mul": mul,
                 "jnz": jnz }

program = []
with open("input23.txt") as f:
    for line in f:
        instr, X, Y = line.strip().split(' ')
        program.append((instructions[instr], X, Y))


cur = 0
while cur < len(program):
    print(program[cur])
    cur += program[cur][0](program[cur][1], program[cur][2])
    print(cur, registers)
#    input()
    
print(multiples)
