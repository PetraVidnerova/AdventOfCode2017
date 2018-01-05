steps = {
    "n" : (1, 0),
    "ne": (0.5, 1),
    "nw": (0.5, -1),
    "s": (-1, 0),
    "sw": (-0.5, -1),
    "se": (-0.5, 1)
}

x, y = 0, 0

commands = input()
commands = commands.split(',')

for cmd in commands:
    x += steps[cmd][0]
    y += steps[cmd][1]

print(x, y)
x, y = abs(x), abs(y)
s = 0 

while (x, y) != (0, 0):
    print(x,y)
    if y>x and x<=0:
        s += 1
        x += 0.5
        y += -1
        continue
    if y>x and x>0:
        s += 1
        x += -0.5
        y += -1
        continue
    if x>=y:
        s += 1
        x += -1 

print(s)
