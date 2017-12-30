register = {}

condition = {
    ">" : lambda a, b: a > b,
    "<" : lambda a, b: a < b,
    "==" : lambda a, b: a == b,
    "!=" : lambda a, b: a != b,
    ">=" : lambda a, b: a >= b,
    "<=" : lambda a, b: a <= b
    }

with open('input08.txt') as f:
    for line in f:
        reg1, op, val, _, right, cond, left = line.strip().split(' ')

        if condition[cond](register.get(right, 0), int(left)):
            if op == "inc":
                register[reg1] = register.get(reg1, 0) + int(val)
            else:
                assert op == "dec"
                register[reg1] = register.get(reg1, 0) - int(val)

print(register)

max = None
for key, val in register.items():
    if max is None or val > max:
        max = val
print(max)
